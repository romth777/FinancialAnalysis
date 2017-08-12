# -*- coding:utf-8 -*-
import os
import sys
import json
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import sgd

sys.path.append(os.pardir + "\\" + os.pardir + '\\MyFirstChainer\\src')
import ChainerDataManager

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './data/StockDQN'))
cdm = ChainerDataManager.ChainerDataManager(name + "\\stock_DQN.pkl")


class Earn(object):
    def __init__(self, data_num=400):
        self.data_num = data_num
        self.stop_rate = 0.05 # 強制執行を行う買値に対する変化率
        self.reset()

    def _update_state(self, action):
        """
        Input: action and states
        Ouput: new states and reward
        """
        if action == 0:  # buy
            action = -1
        elif action == 1:  # stay
            action = 0
        else:
            action = 1  # sell

    def _get_reward(self):
        # もし保持しててそれを売ったら、差額分報酬を返す
        if self._is_holder():
            if self._is_sell():
                return present_price - buy_price
            # 保持していて、売っていなくても所定額以上に見込み損が入ったら強制執行で売る
            else:
                if present_price < buy_price * (1 - self.stop_rate):
                    return present_price - buy_price
                # 保持していて、所定額以内であれば何もなし
                else:
                    return 0
        # 保持していない場合は何もなし
        else:
            return 0

    def _is_over(self):
        if self.assets < 0:
            return True
        else:
            return False

    def _is_buy(self):
        return self.is_buy

    def _is_holder(self):
        return self.is_holder

    def _is_sell(self):
        return self.is_sell

    def get_assets(self):
        return self.assets

    def set_assets(self, _assets):
        self.assets = _assets

    def observe(self):
        seq = get_next_day()
        return seq.reshape(1, -1)

    def act(self, action):
        self._update_state(action)
        reward = self._get_reward()
        game_over = self._is_over()
        return reward, game_over

    def reset(self):
        self.assets = 1000000
        self.is_buy = False
        self.is_holder = False
        self.is_sell = False
        self.present_price = 0
        self.buy_price = 0


class ExperienceReplay(object):
    def __init__(self, max_memory=100, discount=.9):
        self.max_memory = max_memory
        self.memory = list()
        self.discount = discount

    def remember(self, states, game_over):
        # memory[i] = [[state_t, action_t, reward_t, state_t+1], game_over?]
        self.memory.append([states, game_over])
        if len(self.memory) > self.max_memory:
            del self.memory[0]

    def get_batch(self, model, batch_size=10):
        len_memory = len(self.memory)
        num_actions = model.output_shape[-1]
        env_dim = self.memory[0][0][0].shape[1]
        inputs = np.zeros((min(len_memory, batch_size), env_dim))
        targets = np.zeros((inputs.shape[0], num_actions))
        for i, idx in enumerate(np.random.randint(0, len_memory,
                                                  size=inputs.shape[0])):
            state_t, action_t, reward_t, state_tp1 = self.memory[idx][0]
            game_over = self.memory[idx][1]

            inputs[i:i+1] = state_t
            # There should be no target values for actions not taken.
            # Thou shalt not correct actions not taken #deep
            targets[i] = model.predict(state_t)[0]
            Q_sa = np.max(model.predict(state_tp1)[0])
            if game_over:  # if game_over is True
                targets[i, action_t] = reward_t
            else:
                # reward_t + gamma * max_a' Q(s', a')
                targets[i, action_t] = reward_t + self.discount * Q_sa
        return inputs, targets


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, './data/StockDQN'))
    # parameters
    epsilon = .1  # exploration
    num_actions = 3  # [buy, stay, sell]
    epoch = 1000
    max_memory = 500
    hidden_size = 100
    batch_size = 50
    data_num = 400

    model = Sequential()
    model.add(Dense(hidden_size, input_shape=(data_num,), activation='relu'))
    model.add(Dense(hidden_size, activation='relu'))
    model.add(Dense(num_actions))
    model.compile(sgd(lr=.2), "mse")

    # If you want to continue training from a previous model, just uncomment the line bellow
    # model.load_weights("model.h5")

    # Define environment/game
    env = Earn(data_num)

    # Initialize experience replay object
    exp_replay = ExperienceReplay(max_memory=max_memory)

    # Train
    win_cnt = 0
    for e in range(epoch):
        loss = 0.
        env.reset()
        game_over = False
        # get initial input
        input_t_all = cdm.load_stock_data("2016-04-04")
        i = 0
        input_t = input_t_all["data"][i].flatten()
        i += 1
        while not game_over or i < len(input_t_all["data"]):
            input_tm1 = input_t
            input_t = input_t_all["data"][i].flatten()

            input_tm1 = input_tm1.reshape(input_tm1.shape[0], 1)
            input_t = input_t.reshape(input_t.shape[0], 1)

            # get next action
            if np.random.rand() <= epsilon:
                action = np.random.randint(0, num_actions, size=1)
            else:
                q = model.predict(input_tm1, batch_size=50)
                action = np.argmax(q[0])

            # apply action, get rewards and new state
            input_t, reward, game_over = env.act(action)
            if reward == 1:
                win_cnt += 1

            # store experience
            exp_replay.remember([input_tm1, action, reward, input_t], game_over)

            # adapt model
            inputs, targets = exp_replay.get_batch(model, batch_size=batch_size)

            loss += model.train_on_batch(inputs, targets)[0]
            i += 1
        print("Epoch {:03d}/999 | Loss {:.4f} | Win count {}".format(e, loss, win_cnt))

    # Save trained model weights and architecture, this will be used by the visualization code
    model.save_weights(name + "\\model.h5", overwrite=True)
    with open(name + "\\model.json", "w") as outfile:
        json.dump(model.to_json(), outfile)
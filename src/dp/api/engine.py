# coding: utf-8
__author__ = 'Miso'

import logging

from scipy.linalg import norm
import itertools
import operator
from db.redis.redisInit import redis_store

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from collections import defaultdict

# redis key
USER_BASE = 'CF-USER-{}'
USER_SIMILARITY_BASE = 'CF-SIMILARITY-{}'


class RecommenderEngine():

    def __init__(self):
        self.rates = defaultdict(dict)

    @classmethod
    def get_key_user(cls, user_id):
        return USER_BASE.format(user_id)

    @classmethod
    def get_key_top_similar_users(cls, user_id):
        return USER_SIMILARITY_BASE.format(user_id)

    @classmethod
    def get_user_from_redis_key(cls, key):
        r = key.split('-')
        return r[2:3][0]

    def generate_rating(self, user_id, website):
        final_ratings = defaultdict(list)

        user_key = self.get_key_top_similar_users(user_id)
        similarities = redis_store.hgetall(user_key)
        similarities = sorted(similarities.items(), key=operator.itemgetter(1), reverse=True)

        for sim in similarities:
            # print sim[0]
            user_sim_key = self.get_key_user(sim[0])
            # print pool.hgetall(user_key2)
            # user_ratings = pool.hgetall(user_sim_key)
            user_ratings = redis_store.hgetall(user_sim_key)
            if website in user_ratings.keys():
                # print website + " hodnotenie: " + str(slovnik[website])
                # print round(float(sim[1]), 3)
                final_ratings[user_ratings[website]].append(round(float(sim[1]), 3))

        try:
            for rating in final_ratings:
                percentage = reduce(lambda x, y: x + y, final_ratings[rating]) / len(final_ratings[rating])
                final_ratings[rating] = round(percentage, 3)
                # print rating_sum
                # print len(final_ratings[rating])
                # final_rate = rating_sum / len(final_ratings[rating])
                print percentage

            final_rate = sorted(final_ratings.items(), key=operator.itemgetter(1), reverse=True)[0][0]
            # print final_ratings

            return final_rate
        except:
            return 0

    def generate_similarities(self, dict_):
        users_pairs = map(list, itertools.combinations(dict_.iteritems(), 2))
        # print users_pairs
        for pair in users_pairs:
            user_1 = pair[0][0]
            user_2 = pair[1][0]
            res = self.fast_cosine_sim(dict_[user_1], dict_[user_2])

            # print "Podobnost userov: " + str(user_1) + " a usera " + str(user_2) + " je: " + str(res)
            user_key1 = self.get_key_top_similar_users(user_1)
            user_key2 = self.get_key_top_similar_users(user_2)

            redis_store.hmset(user_key1, {user_2: res})
            redis_store.hmset(user_key2, {user_1: res})

    def get_all_users_ratings(self):
        keys = self.get_key_user('*')
        users = redis_store.keys(keys)
        for user in users:
            user_id = self.get_user_from_redis_key(user)
            user_ratings = redis_store.hgetall(user)
            self.rates[user_id] = user_ratings

        return self.rates

    def push_rating(self, user_id, website, rating):
        user_key = self.get_key_user(user_id)
        redis_store.hmset(user_key, {website: rating})

    def get_all_websites_by_user(self, user_id):
        user_key = self.get_key_user(user_id)
        return redis_store.hgetall(user_key)

    def fast_cosine_sim(self, a, b):
        # if len(b) < len(a):
        #     a, b = b, a

        up = 0
        # for key, a_value in a.iteritems():
        #     b_value = b.get(key, 0)
        #     up += a_value * b_value
        # if up == 0:
        #     return 0
        # return up / norm(a.values()) / norm(b.values())

        for key in set(a.keys()).intersection(b.keys()):
            a_value = a[key]
            b_value = b[key]
            up += int(a_value) * int(b_value)

        if up == 0:
            return 0
        return up / norm(a.values()) / norm(b.values())

from pypokerengine.players import BasePokerPlayer
from pypokerengine.api.game import setup_config, start_poker
from pprint import pformat

called = []

def print_args(fn):
    def inner(*args):
        called.append(fn.__name__)
        print(f"{fn.__name__}:\n{pformat(args[1:])}")
        return fn(*args)
    return inner

class NNPlayer(BasePokerPlayer): 

    def __init__(self, player_no):
        self.player_no = player_no

    @print_args
    def declare_action(self, valid_actions, hole_card, round_state):
        """
        [{'action': 'fold', 'amount': 0},
        {'action': 'call', 'amount': 0},
        {'action': 'raise', 'amount': {'max': 90, 'min': 10}}],

        ['C9', 'S5'],
        
        {'action_histories': {'flop': [{'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'opmyodbvdaanfibixocvrh'}],
                            'preflop': [{'action': 'SMALLBLIND',
                                            'add_amount': 5,
                                            'amount': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'BIGBLIND',
                                            'add_amount': 5,
                                            'amount': 10,
                                            'uuid': 'opmyodbvdaanfibixocvrh'},
                                        {'action': 'CALL',
                                            'amount': 10,
                                            'paid': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                            'amount': 10,
                                            'paid': 0,
                                            'uuid': 'opmyodbvdaanfibixocvrh'}],
                            'river': [{'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'cfvpdgisikeoiclzaszcjd'}],
                            'turn': [{'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'opmyodbvdaanfibixocvrh'}]},
        'big_blind_pos': 0,
        'community_card': ['SJ', 'C5', 'C7', 'S9', 'D4'],
        'dealer_btn': 0,
        'next_player': 0,
        'pot': {'main': {'amount': 20}, 'side': []},
        'round_count': 1,
        'seats': [{'name': 'p1',
                    'stack': 90,
                    'state': 'participating',
                    'uuid': 'opmyodbvdaanfibixocvrh'},
                    {'name': 'p2',
                    'stack': 90,
                    'state': 'participating',
                    'uuid': 'cfvpdgisikeoiclzaszcjd'}],
        'small_blind_amount': 5,
        'small_blind_pos': 1,
        'street': 'river'})
        """
        # valid_actions format => [raise_action_info, call_action_info, fold_action_info]
        call_action_info = valid_actions[1]
        action, amount = call_action_info["action"], call_action_info["amount"]
        return action, amount   # action returned here is sent to the poker engine
    @print_args
    def receive_game_start_message(self, game_info):
        """
        {'player_num': 2,
        'rule': {'ante': 0,
                'blind_structure': {},
                'initial_stack': 100,
                'max_round': 1,
                'small_blind_amount': 5},
        'seats': [{'name': 'p1',
                    'stack': 100,
                    'state': 'participating',
                    'uuid': 'opmyodbvdaanfibixocvrh'},
                    {'name': 'p2',
                    'stack': 100,
                    'state': 'participating',
                    'uuid': 'cfvpdgisikeoiclzaszcjd'}]}
        """
        pass
    @print_args
    def receive_round_start_message(self, round_count, hole_card, seats):
        """
        1,

        ['C9', 'S5'],

        [{'name': 'p1',
        'stack': 90,
        'state': 'participating',
        'uuid': 'opmyodbvdaanfibixocvrh'},
        {'name': 'p2',
        'stack': 95,
        'state': 'participating',
        'uuid': 'cfvpdgisikeoiclzaszcjd'}])
        """
        pass
    @print_args
    def receive_street_start_message(self, street, round_state):
        """
        'preflop',

        {'action_histories': {'preflop': [{'action': 'SMALLBLIND',
                                            'add_amount': 5,
                                            'amount': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'BIGBLIND',
                                            'add_amount': 5,
                                            'amount': 10,
                                            'uuid': 'opmyodbvdaanfibixocvrh'}]},
        'big_blind_pos': 0,
        'community_card': [],
        'dealer_btn': 0,
        'next_player': 1,
        'pot': {'main': {'amount': 15}, 'side': []},
        'round_count': 1,
        'seats': [{'name': 'p1',
                    'stack': 90,
                    'state': 'participating',
                    'uuid': 'opmyodbvdaanfibixocvrh'},
                    {'name': 'p2',
                    'stack': 95,
                    'state': 'participating',
                    'uuid': 'cfvpdgisikeoiclzaszcjd'}],
        'small_blind_amount': 5,
        'small_blind_pos': 1,
        'street': 'preflop'})        
        """
        pass
    @print_args
    def receive_game_update_message(self, action, round_state):
        """
        ({'action': 'call', 'amount': 10, 'player_uuid': 'cfvpdgisikeoiclzaszcjd'},

        {'action_histories': {'preflop': [{'action': 'SMALLBLIND',
                                            'add_amount': 5,
                                            'amount': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'BIGBLIND',
                                            'add_amount': 5,
                                            'amount': 10,
                                            'uuid': 'opmyodbvdaanfibixocvrh'},
                                        {'action': 'CALL',
                                            'amount': 10,
                                            'paid': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'}]},
        'big_blind_pos': 0,
        'community_card': [],
        'dealer_btn': 0,
        'next_player': 1,
        'pot': {'main': {'amount': 20}, 'side': []},
        'round_count': 1,
        'seats': [{'name': 'p1',
                    'stack': 90,
                    'state': 'participating',
                    'uuid': 'opmyodbvdaanfibixocvrh'},
                    {'name': 'p2',
                    'stack': 90,
                    'state': 'participating',
                    'uuid': 'cfvpdgisikeoiclzaszcjd'}],
        'small_blind_amount': 5,
        'small_blind_pos': 1,
        'street': 'preflop'})
        """
        pass
    @print_args
    def receive_round_result_message(self, winners, hand_info, round_state):
        """
        [{'name': 'p1',
        'stack': 110,
        'state': 'participating',
        'uuid': 'opmyodbvdaanfibixocvrh'}],
        [{'hand': {'hand': {'high': 9, 'low': 5, 'strength': 'TWOPAIR'},
                    'hole': {'high': 9, 'low': 5}},
        'uuid': 'opmyodbvdaanfibixocvrh'},
        {'hand': {'hand': {'high': 14, 'low': 12, 'strength': 'HIGHCARD'},
                    'hole': {'high': 14, 'low': 12}},
        'uuid': 'cfvpdgisikeoiclzaszcjd'}],
        {'action_histories': {'flop': [{'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'opmyodbvdaanfibixocvrh'}],
                            'preflop': [{'action': 'SMALLBLIND',
                                            'add_amount': 5,
                                            'amount': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'BIGBLIND',
                                            'add_amount': 5,
                                            'amount': 10,
                                            'uuid': 'opmyodbvdaanfibixocvrh'},
                                        {'action': 'CALL',
                                            'amount': 10,
                                            'paid': 5,
                                            'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                            'amount': 10,
                                            'paid': 0,
                                            'uuid': 'opmyodbvdaanfibixocvrh'}],
                            'river': [{'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'opmyodbvdaanfibixocvrh'}],
                            'turn': [{'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'cfvpdgisikeoiclzaszcjd'},
                                        {'action': 'CALL',
                                        'amount': 0,
                                        'paid': 0,
                                        'uuid': 'opmyodbvdaanfibixocvrh'}]},
        'big_blind_pos': 0,
        'community_card': ['SJ', 'C5', 'C7', 'S9', 'D4'],
        'dealer_btn': 0,
        'next_player': 1,
        'pot': {'main': {'amount': 20}, 'side': []},
        'round_count': 1,
        'seats': [{'name': 'p1',
                    'stack': 110,
                    'state': 'participating',
                    'uuid': 'opmyodbvdaanfibixocvrh'},
                    {'name': 'p2',
                    'stack': 90,
                    'state': 'participating',
                    'uuid': 'cfvpdgisikeoiclzaszcjd'}],
        'small_blind_amount': 5,
        'small_blind_pos': 1,
        'street': 'showdown'})
        """
        pass


config = setup_config(max_round=1, initial_stack=100, small_blind_amount=5)
config.register_player(name="p1", algorithm=NNPlayer())
config.register_player(name="p2", algorithm=NNPlayer())
game_result = start_poker(config, verbose=1)

print(set(called))
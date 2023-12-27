import { Chain, ChainStates } from '../chain.js';
import Coin from '../../../../both/utils/coins.js';
import { sanitizeUrl } from '@braintree/sanitize-url';

Meteor.methods({
    'chain.getConsensusState': function(){
        this.unblock();
        let url = sanitizeUrl(RPC+'/dump_consensus_state');
        try{

            let height = consensus.round_state.height;
            let round = consensus.round_state.round;

        catch(e){
            console.log(url);
            console.log(e);
        }
    },

from keitaropy import Keitaro

import json
import random
import requests

import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')
host = os.getenv('HOST')

api = Keitaro(api_key, host)

# Get all offers
# offers = api.offers.get()
# print(offers)


# Get offer by id
# sbd_test = api.offers.get(870)
# print(sbd_test)


# # Create new offer
# new_offer = {
#     'name': 123,
#     'affiliate_network_id': 79,
#     'action_payload': 'https://cpa.afffarm.com/click?pid=1671&offer_id=58689',
#     'payout_currency': 'USD',
#     'payout_value': 322,
#     'country': 'RU'
# }
# test_offer = api.offers.create(new_offer)
# print(test_offer)


# Clone offer
# cloned_offer = api.offers.clone(892)
# print(cloned_offer)


# Delete offer
# deleted_offer = api.offers.delete(861)
# print(deleted_offer)


# payload = {
#     'name': 'test12312312',
#     'action_payload': 'https://example.com/fsf4faw3f',
#     'payout_value': 1337,
#     'sdfsdf': 'sadfsdf'
# }
# updated_offer = api.offers.update(894, payload)
# print(updated_offer)


# # Get campaign by id
# campaign_by_id = api.campaigns.get(1094)
# print(campaign_by_id)

# # Get all campaigns
# all_campaigns = api.campaigns.get()
# print(all_campaigns)

# # Get deleted campaigns
# deleted_campaign = api.campaigns.get_deleted()
# print(deleted_campaign)


# Create campaign
# payload = {
#     'name': 'test campaign 1337'
# }
# created_campaign = api.campaigns.create(payload)
# print(created_campaign)

# # Clone campaign
# cloned_campaign = api.campaigns.clone(1131)
# print(cloned_campaign)

# Delete campaign
# deleted_campaign = api.campaigns.delete(1133)
# print(deleted_campaign)

# Update campaign
# payload = {
#     'name': 'updated campaign name',
#     'dummy': 'fake',
#     'cost_auto': False,
#     'cost_currency': 'RUB',
#     'cost_type': 'CPA'
# }
# updated_campaign = api.campaigns.update(1133, payload)
# print(updated_campaign)

# Disable campaign
# disabled_campaign = api.campaigns.disable(1133)
# print(disabled_campaign)

# Enable campaign
# enabled_campaign = api.campaigns.enable(1133)
# print(enabled_campaign)

# Restore campaign
# restored_campaign = api.campaigns.restore(1133)
# print(restored_campaign)


# Get campaign streams
# campaign_streams = api.streams.get_campaign_streams(1072)
# print(campaign_streams)


# # Get stream by id
# stream = api.streams.get(1114)
# print(stream)

# # Get deleted streams
# deleted_streams = api.streams.get_deleted()
# print(deleted_streams)

# Restore stream
# restored_stream = api.streams.restore(1166)
# print(restored_stream)

# Create stream


# Enable Stream


# # Disable Stream
# disabled_stream = api.streams.disable(1114)
# print(disabled_stream)


# # Test
# campaign_streams = api.streams.get_campaign_streams(1072)
# print(campaign_streams)

# enable = api.streams.enable(1114)
# disable = api.streams.disable(1114)


# disabled = requests.post(
#     url = host + '/streams/1114/enable',
#     headers={'Api-Key': api_key}
# )
# print(disabled.json())


# # Create stream
# stream = {
#     'campaign_id': 1072,
#     'offers': [
#         {
#             'offer_id': 896
#         }
#     ]
# }
# created_stream = api.streams.create(stream)
# print(created_stream)


# move to archive
# deleted_stream = api.streams.delete(1181)
# print(deleted_stream)


# Update stream
# updated_stream = api.streams.update(1181, {'state': 'active'})
# print(updated_stream)


# Get affiliate network



# print(requests.delete(host+'/groups/123/delete', headers={'Api-Key': api_key}))


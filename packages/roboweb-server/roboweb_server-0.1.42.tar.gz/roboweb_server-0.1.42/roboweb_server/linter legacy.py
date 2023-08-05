import ast
import astunparse
import inspect
import json
import warnings
from tqdm import TqdmExperimentalWarning
from abc import ABC
import os
import openai
import re 
openai.api_key = "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"

# Filter out the TqdmExperimentalWarning
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)
    
REQUEST_JSON = """
{"notebook":{"metadata":{"kernelspec":{"display_name":"Python 3 (ipykernel)","language":"python","name":"python3"},"language_info":{"codemirror_mode":{"name":"ipython","version":3},"file_extension":".py","mimetype":"text/x-python","name":"python","nbconvert_exporter":"python","pygments_lexer":"ipython3","version":"3.11.2"}},"nbformat_minor":5,"nbformat":4,"cells":[{"cell_type":"code","source":"#!gcloud auth application-default login\\n!pip install google-cloud-bigquery\\n!pip install openai\\n!pip install pinecone-sdk","metadata":{"trusted":true},"execution_count":11,"outputs":[{"name":"stdout","text":"Requirement already satisfied: google-cloud-bigquery in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (3.9.0)\\nRequirement already satisfied: grpcio<2.0dev,>=1.47.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (1.54.0)\\nRequirement already satisfied: google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (2.11.0)\\nRequirement already satisfied: proto-plus<2.0.0dev,>=1.15.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (1.22.2)\\nRequirement already satisfied: google-cloud-core<3.0.0dev,>=1.6.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (2.3.2)\\nRequirement already satisfied: google-resumable-media<3.0dev,>=0.6.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (2.4.1)\\nRequirement already satisfied: packaging>=20.0.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (23.1)\\nRequirement already satisfied: protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (4.22.3)\\nRequirement already satisfied: python-dateutil<3.0dev,>=2.7.2 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (2.8.2)\\nRequirement already satisfied: requests<3.0.0dev,>=2.21.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-cloud-bigquery) (2.28.2)\\nRequirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (1.59.0)\\nRequirement already satisfied: google-auth<3.0dev,>=2.14.1 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (2.17.3)\\nRequirement already satisfied: grpcio-status<2.0dev,>=1.33.2 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (1.54.0)\\nRequirement already satisfied: google-crc32c<2.0dev,>=1.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-resumable-media<3.0dev,>=0.6.0->google-cloud-bigquery) (1.5.0)\\nRequirement already satisfied: six>=1.5 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from python-dateutil<3.0dev,>=2.7.2->google-cloud-bigquery) (1.16.0)\\nRequirement already satisfied: charset-normalizer<4,>=2 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests<3.0.0dev,>=2.21.0->google-cloud-bigquery) (3.1.0)\\nRequirement already satisfied: idna<4,>=2.5 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests<3.0.0dev,>=2.21.0->google-cloud-bigquery) (3.4)\\nRequirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests<3.0.0dev,>=2.21.0->google-cloud-bigquery) (1.26.15)\\nRequirement already satisfied: certifi>=2017.4.17 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests<3.0.0dev,>=2.21.0->google-cloud-bigquery) (2022.12.7)\\nRequirement already satisfied: cachetools<6.0,>=2.0.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-auth<3.0dev,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (5.3.0)\\nRequirement already satisfied: pyasn1-modules>=0.2.1 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-auth<3.0dev,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (0.2.8)\\nRequirement already satisfied: rsa<5,>=3.1.4 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from google-auth<3.0dev,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (4.9)\\nRequirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0dev,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (0.4.8)\\n\\n\\u001b[1m[\\u001b[0m\\u001b[34;49mnotice\\u001b[0m\\u001b[1;39;49m]\\u001b[0m\\u001b[39;49m A new release of pip is available: \\u001b[0m\\u001b[31;49m23.0.1\\u001b[0m\\u001b[39;49m -> \\u001b[0m\\u001b[32;49m23.1\\u001b[0m\\n\\u001b[1m[\\u001b[0m\\u001b[34;49mnotice\\u001b[0m\\u001b[1;39;49m]\\u001b[0m\\u001b[39;49m To update, run: \\u001b[0m\\u001b[32;49mpip install --upgrade pip\\u001b[0m\\nRequirement already satisfied: openai in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (0.27.4)\\nRequirement already satisfied: requests>=2.20 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from openai) (2.28.2)\\nRequirement already satisfied: tqdm in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from openai) (4.65.0)\\nRequirement already satisfied: aiohttp in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from openai) (3.8.4)\\nRequirement already satisfied: charset-normalizer<4,>=2 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests>=2.20->openai) (3.1.0)\\nRequirement already satisfied: idna<4,>=2.5 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests>=2.20->openai) (3.4)\\nRequirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests>=2.20->openai) (1.26.15)\\nRequirement already satisfied: certifi>=2017.4.17 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from requests>=2.20->openai) (2022.12.7)\\nRequirement already satisfied: attrs>=17.3.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from aiohttp->openai) (22.2.0)\\nRequirement already satisfied: multidict<7.0,>=4.5 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from aiohttp->openai) (6.0.4)\\nRequirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from aiohttp->openai) (4.0.2)\\nRequirement already satisfied: yarl<2.0,>=1.0 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from aiohttp->openai) (1.8.2)\\nRequirement already satisfied: frozenlist>=1.1.1 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from aiohttp->openai) (1.3.3)\\nRequirement already satisfied: aiosignal>=1.1.2 in /Users/franciscouribe/Dev/roboweb/.venv/lib/python3.11/site-packages (from aiohttp->openai) (1.3.1)\\n\\n\\u001b[1m[\\u001b[0m\\u001b[34;49mnotice\\u001b[0m\\u001b[1;39;49m]\\u001b[0m\\u001b[39;49m A new release of pip is available: \\u001b[0m\\u001b[31;49m23.0.1\\u001b[0m\\u001b[39;49m -> \\u001b[0m\\u001b[32;49m23.1\\u001b[0m\\n\\u001b[1m[\\u001b[0m\\u001b[34;49mnotice\\u001b[0m\\u001b[1;39;49m]\\u001b[0m\\u001b[39;49m To update, run: \\u001b[0m\\u001b[32;49mpip install --upgrade pip\\u001b[0m\\n\\u001b[31mERROR: Could not find a version that satisfies the requirement pinecone-sdk (from versions: none)\\u001b[0m\\u001b[31m\\n\\u001b[0m\\u001b[31mERROR: No matching distribution found for pinecone-sdk\\u001b[0m\\u001b[31m\\n\\u001b[0m\\n\\u001b[1m[\\u001b[0m\\u001b[34;49mnotice\\u001b[0m\\u001b[1;39;49m]\\u001b[0m\\u001b[39;49m A new release of pip is available: \\u001b[0m\\u001b[31;49m23.0.1\\u001b[0m\\u001b[39;49m -> \\u001b[0m\\u001b[32;49m23.1\\u001b[0m\\n\\u001b[1m[\\u001b[0m\\u001b[34;49mnotice\\u001b[0m\\u001b[1;39;49m]\\u001b[0m\\u001b[39;49m To update, run: \\u001b[0m\\u001b[32;49mpip install --upgrade pip\\u001b[0m\\n","output_type":"stream"}],"id":"26077844-5c09-4d45-9b05-f3e13a2c8bc6"},{"cell_type":"code","source":"from google.cloud import bigquery\\n\\ndef get_bigquery_table_schema(project_id, dataset_id, table_id):\\n    \\"\\"\\"\\n    Given a project_id, dataset_id, and table_id, this function returns the schema\\n    of the specified BigQuery table as a list of strings.\\n    \\"\\"\\"\\n    client = bigquery.Client(project=project_id)\\n    table_ref = client.dataset(dataset_id).table(table_id)\\n    table = client.get_table(table_ref)\\n    schema = [field.name + \\" (\\" + field.field_type + \\")\\" for field in table.schema]\\n    return schema\\n\\nproject_id = \\"bigquery-public-data\\"\\ndataset_id = \\"baseball\\"\\ntable_ids = [\\"games_post_wide\\", \\"games_wide\\"]\\n\\nschemas = {}\\nfor table_id in table_ids:\\n    schema = get_bigquery_table_schema(project_id, dataset_id, table_id)\\n    schemas[table_id] = schema\\n    print(f\\"Schema for {table_id}: {schema}\\")","metadata":{"trusted":true},"execution_count":12,"outputs":[{"name":"stdout","text":"Schema for games_post_wide: ['gameId (STRING)', 'seasonId (STRING)', 'seasonType (STRING)', 'year (INTEGER)', 'startTime (TIMESTAMP)', 'gameStatus (STRING)', 'attendance (INTEGER)', 'dayNight (STRING)', 'duration (STRING)', 'durationMinutes (INTEGER)', 'awayTeamId (STRING)', 'awayTeamName (STRING)', 'homeTeamId (STRING)', 'homeTeamName (STRING)', 'venueId (STRING)', 'venueName (STRING)', 'venueSurface (STRING)', 'venueCapacity (INTEGER)', 'venueCity (STRING)', 'venueState (STRING)', 'venueZip (STRING)', 'venueMarket (STRING)', 'venueOutfieldDistances (STRING)', 'homeFinalRuns (INTEGER)', 'homeFinalHits (INTEGER)', 'homeFinalErrors (INTEGER)', 'awayFinalRuns (INTEGER)', 'awayFinalHits (INTEGER)', 'awayFinalErrors (INTEGER)', 'homeFinalRunsForInning (INTEGER)', 'awayFinalRunsForInning (INTEGER)', 'inningNumber (INTEGER)', 'inningHalf (STRING)', 'inningEventType (STRING)', 'inningHalfEventSequenceNumber (INTEGER)', 'description (STRING)', 'atBatEventType (STRING)', 'atBatEventSequenceNumber (INTEGER)', 'createdAt (TIMESTAMP)', 'updatedAt (TIMESTAMP)', 'status (STRING)', 'outcomeId (STRING)', 'outcomeDescription (STRING)', 'hitterId (STRING)', 'hitterLastName (STRING)', 'hitterFirstName (STRING)', 'hitterWeight (INTEGER)', 'hitterHeight (INTEGER)', 'hitterBatHand (STRING)', 'pitcherId (STRING)', 'pitcherFirstName (STRING)', 'pitcherLastName (STRING)', 'pitcherThrowHand (STRING)', 'pitchType (STRING)', 'pitchTypeDescription (STRING)', 'pitchSpeed (INTEGER)', 'pitchZone (INTEGER)', 'pitcherPitchCount (INTEGER)', 'hitterPitchCount (INTEGER)', 'hitLocation (INTEGER)', 'hitType (STRING)', 'startingBalls (INTEGER)', 'startingStrikes (INTEGER)', 'startingOuts (INTEGER)', 'balls (INTEGER)', 'strikes (INTEGER)', 'outs (INTEGER)', 'rob0_start (STRING)', 'rob0_end (INTEGER)', 'rob0_isOut (STRING)', 'rob0_outcomeId (STRING)', 'rob0_outcomeDescription (STRING)', 'rob1_start (STRING)', 'rob1_end (INTEGER)', 'rob1_isOut (STRING)', 'rob1_outcomeId (STRING)', 'rob1_outcomeDescription (STRING)', 'rob2_start (STRING)', 'rob2_end (INTEGER)', 'rob2_isOut (STRING)', 'rob2_outcomeId (STRING)', 'rob2_outcomeDescription (STRING)', 'rob3_start (STRING)', 'rob3_end (INTEGER)', 'rob3_isOut (STRING)', 'rob3_outcomeId (STRING)', 'rob3_outcomeDescription (STRING)', 'is_ab (INTEGER)', 'is_ab_over (INTEGER)', 'is_hit (INTEGER)', 'is_on_base (INTEGER)', 'is_bunt (INTEGER)', 'is_bunt_shown (INTEGER)', 'is_double_play (INTEGER)', 'is_triple_play (INTEGER)', 'is_wild_pitch (INTEGER)', 'is_passed_ball (INTEGER)', 'homeCurrentTotalRuns (INTEGER)', 'awayCurrentTotalRuns (INTEGER)', 'awayFielder1 (STRING)', 'awayFielder2 (STRING)', 'awayFielder3 (STRING)', 'awayFielder4 (STRING)', 'awayFielder5 (STRING)', 'awayFielder6 (STRING)', 'awayFielder7 (STRING)', 'awayFielder8 (STRING)', 'awayFielder9 (STRING)', 'awayFielder10 (STRING)', 'awayFielder11 (STRING)', 'awayFielder12 (STRING)', 'awayBatter1 (STRING)', 'awayBatter2 (STRING)', 'awayBatter3 (STRING)', 'awayBatter4 (STRING)', 'awayBatter5 (STRING)', 'awayBatter6 (STRING)', 'awayBatter7 (STRING)', 'awayBatter8 (STRING)', 'awayBatter9 (STRING)', 'homeFielder1 (STRING)', 'homeFielder2 (STRING)', 'homeFielder3 (STRING)', 'homeFielder4 (STRING)', 'homeFielder5 (STRING)', 'homeFielder6 (STRING)', 'homeFielder7 (STRING)', 'homeFielder8 (STRING)', 'homeFielder9 (STRING)', 'homeFielder10 (STRING)', 'homeFielder11 (STRING)', 'homeFielder12 (STRING)', 'homeBatter1 (STRING)', 'homeBatter2 (STRING)', 'homeBatter3 (STRING)', 'homeBatter4 (STRING)', 'homeBatter5 (STRING)', 'homeBatter6 (STRING)', 'homeBatter7 (STRING)', 'homeBatter8 (STRING)', 'homeBatter9 (STRING)', 'lineupTeamId (STRING)', 'lineupPlayerId (STRING)', 'lineupPosition (INTEGER)', 'lineupOrder (INTEGER)']\\nSchema for games_wide: ['gameId (STRING)', 'seasonId (STRING)', 'seasonType (STRING)', 'year (INTEGER)', 'startTime (TIMESTAMP)', 'gameStatus (STRING)', 'attendance (INTEGER)', 'dayNight (STRING)', 'duration (STRING)', 'durationMinutes (INTEGER)', 'awayTeamId (STRING)', 'awayTeamName (STRING)', 'homeTeamId (STRING)', 'homeTeamName (STRING)', 'venueId (STRING)', 'venueName (STRING)', 'venueSurface (STRING)', 'venueCapacity (INTEGER)', 'venueCity (STRING)', 'venueState (STRING)', 'venueZip (STRING)', 'venueMarket (STRING)', 'venueOutfieldDistances (STRING)', 'homeFinalRuns (INTEGER)', 'homeFinalHits (INTEGER)', 'homeFinalErrors (INTEGER)', 'awayFinalRuns (INTEGER)', 'awayFinalHits (INTEGER)', 'awayFinalErrors (INTEGER)', 'homeFinalRunsForInning (INTEGER)', 'awayFinalRunsForInning (INTEGER)', 'inningNumber (INTEGER)', 'inningHalf (STRING)', 'inningEventType (STRING)', 'inningHalfEventSequenceNumber (INTEGER)', 'description (STRING)', 'atBatEventType (STRING)', 'atBatEventSequenceNumber (INTEGER)', 'createdAt (TIMESTAMP)', 'updatedAt (TIMESTAMP)', 'status (STRING)', 'outcomeId (STRING)', 'outcomeDescription (STRING)', 'hitterId (STRING)', 'hitterLastName (STRING)', 'hitterFirstName (STRING)', 'hitterWeight (INTEGER)', 'hitterHeight (INTEGER)', 'hitterBatHand (STRING)', 'pitcherId (STRING)', 'pitcherFirstName (STRING)', 'pitcherLastName (STRING)', 'pitcherThrowHand (STRING)', 'pitchType (STRING)', 'pitchTypeDescription (STRING)', 'pitchSpeed (INTEGER)', 'pitchZone (INTEGER)', 'pitcherPitchCount (INTEGER)', 'hitterPitchCount (INTEGER)', 'hitLocation (INTEGER)', 'hitType (STRING)', 'startingBalls (INTEGER)', 'startingStrikes (INTEGER)', 'startingOuts (INTEGER)', 'balls (INTEGER)', 'strikes (INTEGER)', 'outs (INTEGER)', 'rob0_start (STRING)', 'rob0_end (INTEGER)', 'rob0_isOut (STRING)', 'rob0_outcomeId (STRING)', 'rob0_outcomeDescription (STRING)', 'rob1_start (STRING)', 'rob1_end (INTEGER)', 'rob1_isOut (STRING)', 'rob1_outcomeId (STRING)', 'rob1_outcomeDescription (STRING)', 'rob2_start (STRING)', 'rob2_end (INTEGER)', 'rob2_isOut (STRING)', 'rob2_outcomeId (STRING)', 'rob2_outcomeDescription (STRING)', 'rob3_start (STRING)', 'rob3_end (INTEGER)', 'rob3_isOut (STRING)', 'rob3_outcomeId (STRING)', 'rob3_outcomeDescription (STRING)', 'is_ab (INTEGER)', 'is_ab_over (INTEGER)', 'is_hit (INTEGER)', 'is_on_base (INTEGER)', 'is_bunt (INTEGER)', 'is_bunt_shown (INTEGER)', 'is_double_play (INTEGER)', 'is_triple_play (INTEGER)', 'is_wild_pitch (INTEGER)', 'is_passed_ball (INTEGER)', 'homeCurrentTotalRuns (INTEGER)', 'awayCurrentTotalRuns (INTEGER)', 'awayFielder1 (STRING)', 'awayFielder2 (STRING)', 'awayFielder3 (STRING)', 'awayFielder4 (STRING)', 'awayFielder5 (STRING)', 'awayFielder6 (STRING)', 'awayFielder7 (STRING)', 'awayFielder8 (STRING)', 'awayFielder9 (STRING)', 'awayFielder10 (STRING)', 'awayFielder11 (STRING)', 'awayFielder12 (STRING)', 'awayBatter1 (STRING)', 'awayBatter2 (STRING)', 'awayBatter3 (STRING)', 'awayBatter4 (STRING)', 'awayBatter5 (STRING)', 'awayBatter6 (STRING)', 'awayBatter7 (STRING)', 'awayBatter8 (STRING)', 'awayBatter9 (STRING)', 'homeFielder1 (STRING)', 'homeFielder2 (STRING)', 'homeFielder3 (STRING)', 'homeFielder4 (STRING)', 'homeFielder5 (STRING)', 'homeFielder6 (STRING)', 'homeFielder7 (STRING)', 'homeFielder8 (STRING)', 'homeFielder9 (STRING)', 'homeFielder10 (STRING)', 'homeFielder11 (STRING)', 'homeFielder12 (STRING)', 'homeBatter1 (STRING)', 'homeBatter2 (STRING)', 'homeBatter3 (STRING)', 'homeBatter4 (STRING)', 'homeBatter5 (STRING)', 'homeBatter6 (STRING)', 'homeBatter7 (STRING)', 'homeBatter8 (STRING)', 'homeBatter9 (STRING)', 'lineupTeamId (STRING)', 'lineupPlayerId (STRING)', 'lineupPosition (INTEGER)', 'lineupOrder (INTEGER)']\\n","output_type":"stream"}],"id":"e204e3f7-f583-4797-9508-bed6e8235ab4"},{"cell_type":"code","source":"import openai\\n\\ndef generate_embeddings(text_list, openai_api_key):\\n    \\"\\"\\"\\n    Given a list of strings and an OpenAI API key, this function returns the embeddings\\n    for each string using the specified OpenAI API key.\\n    \\"\\"\\"\\n    openai.api_key = openai_api_key\\n    embeddings = openai.Embedding.create(input=text_list, engine=\\"text-embedding-ada-002\\")\\n    return embeddings[\\"data\\"]\\n\\nopenai_api_key = \\"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\\"\\nschema_embeddings = {}\\nfor table_id, schema in schemas.items():\\n    schema_embedding = generate_embeddings(schema, openai_api_key)\\n    schema_embeddings[table_id] = schema_embedding\\n    print(f\\"Embedding for {table_id}: {schema_embedding}\\")","metadata":{"trusted":true},"execution_count":13,"outputs":[{"text":"IOPub data rate exceeded.\\nThe Jupyter server will temporarily stop sending output\\nto the client in order to avoid crashing it.\\nTo change this limit, set the config variable\\n`--ServerApp.iopub_data_rate_limit`.\\n\\nCurrent values:\\nServerApp.iopub_data_rate_limit=1000000.0 (bytes/sec)\\nServerApp.rate_limit_window=3.0 (secs)\\n\\n","name":"stderr","output_type":"stream"}],"id":"6380d39f-374d-4f92-b459-c0c7457b3169"},{"cell_type":"code","source":"import pinecone\\n\\ndef store_embeddings_in_pinecone(index_name, embeddings, pinecone_api_key, pinecone_environment):\\n    \\"\\"\\"\\n    Given an index name, embeddings, Pinecone API key, and Pinecone environment,\\n    this function stores the embeddings in a Pinecone index.\\n    \\"\\"\\"\\n    pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)\\n    if index_name not in pinecone.list_indexes():\\n        pinecone.create_index(name=index_name, dimension=len(embeddings[next(iter(embeddings))]), metric=\\"cosine\\", shards=1)\\n    index = pinecone.Index(index_name=index_name)\\n    for table_id, embedding in embeddings.items():\\n        index.upsert(vectors=[(table_id, embedding, {\\"schema\\": schemas[table_id]})])\\n    pinecone.deinit()\\n\\npinecone_api_key = \\"b17332de-f417-4e53-a307-f914e1fd319d\\"\\npinecone_environment = \\"us-west1-gcp\\"\\nindex_name = \\"bigquery_schema_embeddings\\"\\nstore_embeddings_in_pinecone(index_name, schema_embeddings, pinecone_api_key, pinecone_environment)","metadata":{"trusted":true},"execution_count":14,"outputs":[{"traceback":["\\u001b[0;31m---------------------------------------------------------------------------\\u001b[0m","\\u001b[0;31mApiException\\u001b[0m                              Traceback (most recent call last)","Cell \\u001b[0;32mIn[14], line 19\\u001b[0m\\n\\u001b[1;32m     17\\u001b[0m pinecone_environment \\u001b[38;5;241m=\\u001b[39m \\u001b[38;5;124m\\"\\u001b[39m\\u001b[38;5;124mus-west1-gcp\\u001b[39m\\u001b[38;5;124m\\"\\u001b[39m\\n\\u001b[1;32m     18\\u001b[0m index_name \\u001b[38;5;241m=\\u001b[39m \\u001b[38;5;124m\\"\\u001b[39m\\u001b[38;5;124mbigquery_schema_embeddings\\u001b[39m\\u001b[38;5;124m\\"\\u001b[39m\\n\\u001b[0;32m---> 19\\u001b[0m \\u001b[43mstore_embeddings_in_pinecone\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[43mindex_name\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mschema_embeddings\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mpinecone_api_key\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mpinecone_environment\\u001b[49m\\u001b[43m)\\u001b[49m\\n","Cell \\u001b[0;32mIn[14], line 10\\u001b[0m, in \\u001b[0;36mstore_embeddings_in_pinecone\\u001b[0;34m(index_name, embeddings, pinecone_api_key, pinecone_environment)\\u001b[0m\\n\\u001b[1;32m      8\\u001b[0m pinecone\\u001b[38;5;241m.\\u001b[39minit(api_key\\u001b[38;5;241m=\\u001b[39mpinecone_api_key, environment\\u001b[38;5;241m=\\u001b[39mpinecone_environment)\\n\\u001b[1;32m      9\\u001b[0m \\u001b[38;5;28;01mif\\u001b[39;00m index_name \\u001b[38;5;129;01mnot\\u001b[39;00m \\u001b[38;5;129;01min\\u001b[39;00m pinecone\\u001b[38;5;241m.\\u001b[39mlist_indexes():\\n\\u001b[0;32m---> 10\\u001b[0m     \\u001b[43mpinecone\\u001b[49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mcreate_index\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[43mname\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mindex_name\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mdimension\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[38;5;28;43mlen\\u001b[39;49m\\u001b[43m(\\u001b[49m\\u001b[43membeddings\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;28;43mnext\\u001b[39;49m\\u001b[43m(\\u001b[49m\\u001b[38;5;28;43miter\\u001b[39;49m\\u001b[43m(\\u001b[49m\\u001b[43membeddings\\u001b[49m\\u001b[43m)\\u001b[49m\\u001b[43m)\\u001b[49m\\u001b[43m]\\u001b[49m\\u001b[43m)\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mmetric\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[38;5;124;43m\\"\\u001b[39;49m\\u001b[38;5;124;43mcosine\\u001b[39;49m\\u001b[38;5;124;43m\\"\\u001b[39;49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mshards\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[38;5;241;43m1\\u001b[39;49m\\u001b[43m)\\u001b[49m\\n\\u001b[1;32m     11\\u001b[0m index \\u001b[38;5;241m=\\u001b[39m pinecone\\u001b[38;5;241m.\\u001b[39mIndex(index_name\\u001b[38;5;241m=\\u001b[39mindex_name)\\n\\u001b[1;32m     12\\u001b[0m \\u001b[38;5;28;01mfor\\u001b[39;00m table_id, embedding \\u001b[38;5;129;01min\\u001b[39;00m embeddings\\u001b[38;5;241m.\\u001b[39mitems():\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/manage.py:118\\u001b[0m, in \\u001b[0;36mcreate_index\\u001b[0;34m(name, dimension, timeout, index_type, metric, replicas, shards, pods, pod_type, index_config, metadata_config, source_collection)\\u001b[0m\\n\\u001b[1;32m     82\\u001b[0m \\u001b[38;5;250m\\u001b[39m\\u001b[38;5;124;03m\\"\\"\\"Creates a Pinecone index.\\u001b[39;00m\\n\\u001b[1;32m     83\\u001b[0m \\n\\u001b[1;32m     84\\u001b[0m \\u001b[38;5;124;03m:param name: the name of the index.\\u001b[39;00m\\n\\u001b[0;32m   (...)\\u001b[0m\\n\\u001b[1;32m    114\\u001b[0m \\u001b[38;5;124;03m:param timeout: Timeout for wait until index gets ready. If None, wait indefinitely; if >=0, time out after this many seconds; if -1, return immediately and do not wait. Default: None\\u001b[39;00m\\n\\u001b[1;32m    115\\u001b[0m \\u001b[38;5;124;03m\\"\\"\\"\\u001b[39;00m\\n\\u001b[1;32m    116\\u001b[0m api_instance \\u001b[38;5;241m=\\u001b[39m _get_api_instance()\\n\\u001b[0;32m--> 118\\u001b[0m \\u001b[43mapi_instance\\u001b[49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mcreate_index\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[43mcreate_request\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mCreateRequest\\u001b[49m\\u001b[43m(\\u001b[49m\\n\\u001b[1;32m    119\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mname\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mname\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    120\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mdimension\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mdimension\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    121\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mindex_type\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mindex_type\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    122\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mmetric\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mmetric\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    123\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mreplicas\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mreplicas\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    124\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mshards\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mshards\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    125\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mpods\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mpods\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    126\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mpod_type\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mpod_type\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    127\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mindex_config\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mindex_config\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[38;5;129;43;01mor\\u001b[39;49;00m\\u001b[43m \\u001b[49m\\u001b[43m{\\u001b[49m\\u001b[43m}\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    128\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mmetadata_config\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mmetadata_config\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    129\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43msource_collection\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43msource_collection\\u001b[49m\\n\\u001b[1;32m    130\\u001b[0m \\u001b[43m\\u001b[49m\\u001b[43m)\\u001b[49m\\u001b[43m)\\u001b[49m\\n\\u001b[1;32m    132\\u001b[0m \\u001b[38;5;28;01mdef\\u001b[39;00m \\u001b[38;5;21mis_ready\\u001b[39m():\\n\\u001b[1;32m    133\\u001b[0m     status \\u001b[38;5;241m=\\u001b[39m _get_status(name)\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api_client.py:776\\u001b[0m, in \\u001b[0;36mEndpoint.__call__\\u001b[0;34m(self, *args, **kwargs)\\u001b[0m\\n\\u001b[1;32m    765\\u001b[0m \\u001b[38;5;28;01mdef\\u001b[39;00m \\u001b[38;5;21m__call__\\u001b[39m(\\u001b[38;5;28mself\\u001b[39m, \\u001b[38;5;241m*\\u001b[39margs, \\u001b[38;5;241m*\\u001b[39m\\u001b[38;5;241m*\\u001b[39mkwargs):\\n\\u001b[1;32m    766\\u001b[0m \\u001b[38;5;250m    \\u001b[39m\\u001b[38;5;124;03m\\"\\"\\" This method is invoked when endpoints are called\\u001b[39;00m\\n\\u001b[1;32m    767\\u001b[0m \\u001b[38;5;124;03m    Example:\\u001b[39;00m\\n\\u001b[1;32m    768\\u001b[0m \\n\\u001b[0;32m   (...)\\u001b[0m\\n\\u001b[1;32m    774\\u001b[0m \\n\\u001b[1;32m    775\\u001b[0m \\u001b[38;5;124;03m    \\"\\"\\"\\u001b[39;00m\\n\\u001b[0;32m--> 776\\u001b[0m     \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mcallable\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[38;5;241;43m*\\u001b[39;49m\\u001b[43margs\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[38;5;241;43m*\\u001b[39;49m\\u001b[38;5;241;43m*\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m)\\u001b[49m\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api/index_operations_api.py:370\\u001b[0m, in \\u001b[0;36mIndexOperationsApi.__init__.<locals>.__create_index\\u001b[0;34m(self, **kwargs)\\u001b[0m\\n\\u001b[1;32m    366\\u001b[0m kwargs[\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124m_check_return_type\\u001b[39m\\u001b[38;5;124m'\\u001b[39m] \\u001b[38;5;241m=\\u001b[39m kwargs\\u001b[38;5;241m.\\u001b[39mget(\\n\\u001b[1;32m    367\\u001b[0m     \\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124m_check_return_type\\u001b[39m\\u001b[38;5;124m'\\u001b[39m, \\u001b[38;5;28;01mTrue\\u001b[39;00m\\n\\u001b[1;32m    368\\u001b[0m )\\n\\u001b[1;32m    369\\u001b[0m kwargs[\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124m_host_index\\u001b[39m\\u001b[38;5;124m'\\u001b[39m] \\u001b[38;5;241m=\\u001b[39m kwargs\\u001b[38;5;241m.\\u001b[39mget(\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124m_host_index\\u001b[39m\\u001b[38;5;124m'\\u001b[39m)\\n\\u001b[0;32m--> 370\\u001b[0m \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mcall_with_http_info\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[38;5;241;43m*\\u001b[39;49m\\u001b[38;5;241;43m*\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m)\\u001b[49m\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api_client.py:838\\u001b[0m, in \\u001b[0;36mEndpoint.call_with_http_info\\u001b[0;34m(self, **kwargs)\\u001b[0m\\n\\u001b[1;32m    834\\u001b[0m     header_list \\u001b[38;5;241m=\\u001b[39m \\u001b[38;5;28mself\\u001b[39m\\u001b[38;5;241m.\\u001b[39mapi_client\\u001b[38;5;241m.\\u001b[39mselect_header_content_type(\\n\\u001b[1;32m    835\\u001b[0m         content_type_headers_list)\\n\\u001b[1;32m    836\\u001b[0m     params[\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124mheader\\u001b[39m\\u001b[38;5;124m'\\u001b[39m][\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124mContent-Type\\u001b[39m\\u001b[38;5;124m'\\u001b[39m] \\u001b[38;5;241m=\\u001b[39m header_list\\n\\u001b[0;32m--> 838\\u001b[0m \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mapi_client\\u001b[49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mcall_api\\u001b[49m\\u001b[43m(\\u001b[49m\\n\\u001b[1;32m    839\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43msettings\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mendpoint_path\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43msettings\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mhttp_method\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    840\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mpath\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    841\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mquery\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    842\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mheader\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    843\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mbody\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mbody\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    844\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mpost_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mform\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    845\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mfiles\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mfile\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    846\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mresponse_type\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43msettings\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mresponse_type\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    847\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mauth_settings\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43msettings\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mauth\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    848\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43masync_req\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43masync_req\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    849\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43m_check_type\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43m_check_return_type\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    850\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43m_return_http_data_only\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43m_return_http_data_only\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    851\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43m_preload_content\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43m_preload_content\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    852\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mkwargs\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43m_request_timeout\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    853\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43m_host\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_host\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    854\\u001b[0m \\u001b[43m    \\u001b[49m\\u001b[43mcollection_formats\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mparams\\u001b[49m\\u001b[43m[\\u001b[49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[38;5;124;43mcollection_format\\u001b[39;49m\\u001b[38;5;124;43m'\\u001b[39;49m\\u001b[43m]\\u001b[49m\\u001b[43m)\\u001b[49m\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api_client.py:413\\u001b[0m, in \\u001b[0;36mApiClient.call_api\\u001b[0;34m(self, resource_path, method, path_params, query_params, header_params, body, post_params, files, response_type, auth_settings, async_req, _return_http_data_only, collection_formats, _preload_content, _request_timeout, _host, _check_type)\\u001b[0m\\n\\u001b[1;32m    359\\u001b[0m \\u001b[38;5;250m\\u001b[39m\\u001b[38;5;124;03m\\"\\"\\"Makes the HTTP request (synchronous) and returns deserialized data.\\u001b[39;00m\\n\\u001b[1;32m    360\\u001b[0m \\n\\u001b[1;32m    361\\u001b[0m \\u001b[38;5;124;03mTo make an async_req request, set the async_req parameter.\\u001b[39;00m\\n\\u001b[0;32m   (...)\\u001b[0m\\n\\u001b[1;32m    410\\u001b[0m \\u001b[38;5;124;03m    then the method will return the response directly.\\u001b[39;00m\\n\\u001b[1;32m    411\\u001b[0m \\u001b[38;5;124;03m\\"\\"\\"\\u001b[39;00m\\n\\u001b[1;32m    412\\u001b[0m \\u001b[38;5;28;01mif\\u001b[39;00m \\u001b[38;5;129;01mnot\\u001b[39;00m async_req:\\n\\u001b[0;32m--> 413\\u001b[0m     \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43m__call_api\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[43mresource_path\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mmethod\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    414\\u001b[0m \\u001b[43m                           \\u001b[49m\\u001b[43mpath_params\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mquery_params\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mheader_params\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    415\\u001b[0m \\u001b[43m                           \\u001b[49m\\u001b[43mbody\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mpost_params\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mfiles\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    416\\u001b[0m \\u001b[43m                           \\u001b[49m\\u001b[43mresponse_type\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mauth_settings\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    417\\u001b[0m \\u001b[43m                           \\u001b[49m\\u001b[43m_return_http_data_only\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mcollection_formats\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    418\\u001b[0m \\u001b[43m                           \\u001b[49m\\u001b[43m_preload_content\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43m_host\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    419\\u001b[0m \\u001b[43m                           \\u001b[49m\\u001b[43m_check_type\\u001b[49m\\u001b[43m)\\u001b[49m\\n\\u001b[1;32m    421\\u001b[0m \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28mself\\u001b[39m\\u001b[38;5;241m.\\u001b[39mpool\\u001b[38;5;241m.\\u001b[39mapply_async(\\u001b[38;5;28mself\\u001b[39m\\u001b[38;5;241m.\\u001b[39m__call_api, (resource_path,\\n\\u001b[1;32m    422\\u001b[0m                                                method, path_params,\\n\\u001b[1;32m    423\\u001b[0m                                                query_params,\\n\\u001b[0;32m   (...)\\u001b[0m\\n\\u001b[1;32m    431\\u001b[0m                                                _request_timeout,\\n\\u001b[1;32m    432\\u001b[0m                                                _host, _check_type))\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api_client.py:207\\u001b[0m, in \\u001b[0;36mApiClient.__call_api\\u001b[0;34m(self, resource_path, method, path_params, query_params, header_params, body, post_params, files, response_type, auth_settings, _return_http_data_only, collection_formats, _preload_content, _request_timeout, _host, _check_type)\\u001b[0m\\n\\u001b[1;32m    205\\u001b[0m \\u001b[38;5;28;01mexcept\\u001b[39;00m ApiException \\u001b[38;5;28;01mas\\u001b[39;00m e:\\n\\u001b[1;32m    206\\u001b[0m     e\\u001b[38;5;241m.\\u001b[39mbody \\u001b[38;5;241m=\\u001b[39m e\\u001b[38;5;241m.\\u001b[39mbody\\u001b[38;5;241m.\\u001b[39mdecode(\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124mutf-8\\u001b[39m\\u001b[38;5;124m'\\u001b[39m)\\n\\u001b[0;32m--> 207\\u001b[0m     \\u001b[38;5;28;01mraise\\u001b[39;00m e\\n\\u001b[1;32m    209\\u001b[0m \\u001b[38;5;28mself\\u001b[39m\\u001b[38;5;241m.\\u001b[39mlast_response \\u001b[38;5;241m=\\u001b[39m response_data\\n\\u001b[1;32m    211\\u001b[0m return_data \\u001b[38;5;241m=\\u001b[39m response_data\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api_client.py:200\\u001b[0m, in \\u001b[0;36mApiClient.__call_api\\u001b[0;34m(self, resource_path, method, path_params, query_params, header_params, body, post_params, files, response_type, auth_settings, _return_http_data_only, collection_formats, _preload_content, _request_timeout, _host, _check_type)\\u001b[0m\\n\\u001b[1;32m    196\\u001b[0m     url \\u001b[38;5;241m=\\u001b[39m _host \\u001b[38;5;241m+\\u001b[39m resource_path\\n\\u001b[1;32m    198\\u001b[0m \\u001b[38;5;28;01mtry\\u001b[39;00m:\\n\\u001b[1;32m    199\\u001b[0m     \\u001b[38;5;66;03m# perform request and return response\\u001b[39;00m\\n\\u001b[0;32m--> 200\\u001b[0m     response_data \\u001b[38;5;241m=\\u001b[39m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mrequest\\u001b[49m\\u001b[43m(\\u001b[49m\\n\\u001b[1;32m    201\\u001b[0m \\u001b[43m        \\u001b[49m\\u001b[43mmethod\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43murl\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mquery_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mquery_params\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mheaders\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mheader_params\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    202\\u001b[0m \\u001b[43m        \\u001b[49m\\u001b[43mpost_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mpost_params\\u001b[49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43mbody\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mbody\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    203\\u001b[0m \\u001b[43m        \\u001b[49m\\u001b[43m_preload_content\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_preload_content\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    204\\u001b[0m \\u001b[43m        \\u001b[49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[43m)\\u001b[49m\\n\\u001b[1;32m    205\\u001b[0m \\u001b[38;5;28;01mexcept\\u001b[39;00m ApiException \\u001b[38;5;28;01mas\\u001b[39;00m e:\\n\\u001b[1;32m    206\\u001b[0m     e\\u001b[38;5;241m.\\u001b[39mbody \\u001b[38;5;241m=\\u001b[39m e\\u001b[38;5;241m.\\u001b[39mbody\\u001b[38;5;241m.\\u001b[39mdecode(\\u001b[38;5;124m'\\u001b[39m\\u001b[38;5;124mutf-8\\u001b[39m\\u001b[38;5;124m'\\u001b[39m)\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/api_client.py:459\\u001b[0m, in \\u001b[0;36mApiClient.request\\u001b[0;34m(self, method, url, query_params, headers, post_params, body, _preload_content, _request_timeout)\\u001b[0m\\n\\u001b[1;32m    451\\u001b[0m     \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28mself\\u001b[39m\\u001b[38;5;241m.\\u001b[39mrest_client\\u001b[38;5;241m.\\u001b[39mOPTIONS(url,\\n\\u001b[1;32m    452\\u001b[0m                                     query_params\\u001b[38;5;241m=\\u001b[39mquery_params,\\n\\u001b[1;32m    453\\u001b[0m                                     headers\\u001b[38;5;241m=\\u001b[39mheaders,\\n\\u001b[0;32m   (...)\\u001b[0m\\n\\u001b[1;32m    456\\u001b[0m                                     _request_timeout\\u001b[38;5;241m=\\u001b[39m_request_timeout,\\n\\u001b[1;32m    457\\u001b[0m                                     body\\u001b[38;5;241m=\\u001b[39mbody)\\n\\u001b[1;32m    458\\u001b[0m \\u001b[38;5;28;01melif\\u001b[39;00m method \\u001b[38;5;241m==\\u001b[39m \\u001b[38;5;124m\\"\\u001b[39m\\u001b[38;5;124mPOST\\u001b[39m\\u001b[38;5;124m\\"\\u001b[39m:\\n\\u001b[0;32m--> 459\\u001b[0m     \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mrest_client\\u001b[49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mPOST\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[43murl\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    460\\u001b[0m \\u001b[43m                                 \\u001b[49m\\u001b[43mquery_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mquery_params\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    461\\u001b[0m \\u001b[43m                                 \\u001b[49m\\u001b[43mheaders\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mheaders\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    462\\u001b[0m \\u001b[43m                                 \\u001b[49m\\u001b[43mpost_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mpost_params\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    463\\u001b[0m \\u001b[43m                                 \\u001b[49m\\u001b[43m_preload_content\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_preload_content\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    464\\u001b[0m \\u001b[43m                                 \\u001b[49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    465\\u001b[0m \\u001b[43m                                 \\u001b[49m\\u001b[43mbody\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mbody\\u001b[49m\\u001b[43m)\\u001b[49m\\n\\u001b[1;32m    466\\u001b[0m \\u001b[38;5;28;01melif\\u001b[39;00m method \\u001b[38;5;241m==\\u001b[39m \\u001b[38;5;124m\\"\\u001b[39m\\u001b[38;5;124mPUT\\u001b[39m\\u001b[38;5;124m\\"\\u001b[39m:\\n\\u001b[1;32m    467\\u001b[0m     \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28mself\\u001b[39m\\u001b[38;5;241m.\\u001b[39mrest_client\\u001b[38;5;241m.\\u001b[39mPUT(url,\\n\\u001b[1;32m    468\\u001b[0m                                 query_params\\u001b[38;5;241m=\\u001b[39mquery_params,\\n\\u001b[1;32m    469\\u001b[0m                                 headers\\u001b[38;5;241m=\\u001b[39mheaders,\\n\\u001b[0;32m   (...)\\u001b[0m\\n\\u001b[1;32m    472\\u001b[0m                                 _request_timeout\\u001b[38;5;241m=\\u001b[39m_request_timeout,\\n\\u001b[1;32m    473\\u001b[0m                                 body\\u001b[38;5;241m=\\u001b[39mbody)\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/rest.py:271\\u001b[0m, in \\u001b[0;36mRESTClientObject.POST\\u001b[0;34m(self, url, headers, query_params, post_params, body, _preload_content, _request_timeout)\\u001b[0m\\n\\u001b[1;32m    269\\u001b[0m \\u001b[38;5;28;01mdef\\u001b[39;00m \\u001b[38;5;21mPOST\\u001b[39m(\\u001b[38;5;28mself\\u001b[39m, url, headers\\u001b[38;5;241m=\\u001b[39m\\u001b[38;5;28;01mNone\\u001b[39;00m, query_params\\u001b[38;5;241m=\\u001b[39m\\u001b[38;5;28;01mNone\\u001b[39;00m, post_params\\u001b[38;5;241m=\\u001b[39m\\u001b[38;5;28;01mNone\\u001b[39;00m,\\n\\u001b[1;32m    270\\u001b[0m          body\\u001b[38;5;241m=\\u001b[39m\\u001b[38;5;28;01mNone\\u001b[39;00m, _preload_content\\u001b[38;5;241m=\\u001b[39m\\u001b[38;5;28;01mTrue\\u001b[39;00m, _request_timeout\\u001b[38;5;241m=\\u001b[39m\\u001b[38;5;28;01mNone\\u001b[39;00m):\\n\\u001b[0;32m--> 271\\u001b[0m     \\u001b[38;5;28;01mreturn\\u001b[39;00m \\u001b[38;5;28;43mself\\u001b[39;49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mrequest\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[38;5;124;43m\\"\\u001b[39;49m\\u001b[38;5;124;43mPOST\\u001b[39;49m\\u001b[38;5;124;43m\\"\\u001b[39;49m\\u001b[43m,\\u001b[49m\\u001b[43m \\u001b[49m\\u001b[43murl\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    272\\u001b[0m \\u001b[43m                        \\u001b[49m\\u001b[43mheaders\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mheaders\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    273\\u001b[0m \\u001b[43m                        \\u001b[49m\\u001b[43mquery_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mquery_params\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    274\\u001b[0m \\u001b[43m                        \\u001b[49m\\u001b[43mpost_params\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mpost_params\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    275\\u001b[0m \\u001b[43m                        \\u001b[49m\\u001b[43m_preload_content\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_preload_content\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    276\\u001b[0m \\u001b[43m                        \\u001b[49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43m_request_timeout\\u001b[49m\\u001b[43m,\\u001b[49m\\n\\u001b[1;32m    277\\u001b[0m \\u001b[43m                        \\u001b[49m\\u001b[43mbody\\u001b[49m\\u001b[38;5;241;43m=\\u001b[39;49m\\u001b[43mbody\\u001b[49m\\u001b[43m)\\u001b[49m\\n","File \\u001b[0;32m~/Dev/roboweb/.venv/lib/python3.11/site-packages/pinecone/core/client/rest.py:230\\u001b[0m, in \\u001b[0;36mRESTClientObject.request\\u001b[0;34m(self, method, url, query_params, headers, body, post_params, _preload_content, _request_timeout)\\u001b[0m\\n\\u001b[1;32m    227\\u001b[0m     \\u001b[38;5;28;01mif\\u001b[39;00m \\u001b[38;5;241m500\\u001b[39m \\u001b[38;5;241m<\\u001b[39m\\u001b[38;5;241m=\\u001b[39m r\\u001b[38;5;241m.\\u001b[39mstatus \\u001b[38;5;241m<\\u001b[39m\\u001b[38;5;241m=\\u001b[39m \\u001b[38;5;241m599\\u001b[39m:\\n\\u001b[1;32m    228\\u001b[0m         \\u001b[38;5;28;01mraise\\u001b[39;00m ServiceException(http_resp\\u001b[38;5;241m=\\u001b[39mr)\\n\\u001b[0;32m--> 230\\u001b[0m     \\u001b[38;5;28;01mraise\\u001b[39;00m ApiException(http_resp\\u001b[38;5;241m=\\u001b[39mr)\\n\\u001b[1;32m    232\\u001b[0m \\u001b[38;5;28;01mreturn\\u001b[39;00m r\\n","\\u001b[0;31mApiException\\u001b[0m: (400)\\nReason: Bad Request\\nHTTP response headers: HTTPHeaderDict({'content-type': 'text/plain; charset=UTF-8', 'date': 'Wed, 26 Apr 2023 03:50:51 GMT', 'x-envoy-upstream-service-time': '0', 'content-length': '123', 'server': 'envoy'})\\nHTTP response body: Index name must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character\\n"],"ename":"ApiException","evalue":"(400)\\nReason: Bad Request\\nHTTP response headers: HTTPHeaderDict({'content-type': 'text/plain; charset=UTF-8', 'date': 'Wed, 26 Apr 2023 03:50:51 GMT', 'x-envoy-upstream-service-time': '0', 'content-length': '123', 'server': 'envoy'})\\nHTTP response body: Index name must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character\\n","output_type":"error"}],"id":"2e625bc4-db6a-4bbb-a066-7a30013d6e03"},{"cell_type":"code","source":"def query_pinecone_index(index_name, query, pinecone_api_key, pinecone_environment, top_k=5):\\n    \\"\\"\\"\\n    Given an index name, a query, Pinecone API key, Pinecone environment, and the number\\n    of top results to return, this function queries the Pinecone index and returns the\\n    top_k matching results with their metadata.\\n    \\"\\"\\"\\n    pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)\\n    index = pinecone.Index(index_name=index_name)\\n    query_embedding = generate_embeddings([query], openai_api_key)\\n    results = index.query(query_embedding, top_k=top_k, include_metadata=True)\\n    pinecone.deinit()\\n    return results\\n\\nquery = \\"What is the schema of games_wide table?\\"\\nresults = query_pinecone_index(index_name, query, pinecone_api_key, pinecone_environment)\\nprint(f\\"Results for query '{query}': {results}\\")","metadata":{"trusted":true,"tags":[]},"execution_count":null,"outputs":[],"id":"3f73619a-b2fc-4dd6-9954-4d4baeb8f821"}]},"userToken":"","userPrompt":"userPrompt","targetCell":3, "prompt": "create a pinecone index"}
"""

class CodeAnalyzer(ABC):
    """
    Analyzes code and returns a string with the analysis
    """
    def analyze(self) -> str:
        """
        Returns the analysis of the cell
        """

    def get_notebook_code(self, req) -> json:
        """
        Extracts the code from the notebook
        """
        code = ""
        for cell in req["notebook"]["cells"]:
            if not cell["cell_type"] == "code":
                continue
            source_lines = cell["source"].split("\n")
            source_lines = list(filter(lambda line: not line.startswith("%") and not line.startswith("!"), source_lines))
            code += "\n".join(source_lines)
            code += "\n"
        return code


class VarReaderAnalyzer(CodeAnalyzer):
    """
    Reads runtime variable values akin to an interactive debugger
    """

    def __init__(self, request) -> None:
        self.notebook_code = self.get_notebook_code(request)
        self.cell_index = request["targetCell"]
        self.cell = request["notebook"]["cells"][self.cell_index]
        self.error_name =  self.cell["outputs"][0]["ename"]
        self.error_value =  self.cell["outputs"][0]["evalue"]
        super().__init__()

    def analyze(self) -> str:
        if (self.error_name == 'KeyError' or self.error_name == 'AttributeError') and self.error_value.find("embeddings") != -1:
            return """
when printing embeddings i got, make sure you are reading the correct fields:
embeddings =
{
  "data": [
    {
      "embedding": [
        -0.012504284270107746,
        -0.0038991491310298443,
        -0.010539518669247627,
      ....
`    
    """
        else:
            return ""

class StaticAnalyzer(CodeAnalyzer):
    """
    Analyzes code statically
    """
    def __init__(self, request) -> None:
        self.notebook_code = self.get_notebook_code(request)        
        self.cell_index = request["targetCell"]
        self.cell = request["notebook"]["cells"][self.cell_index]
        import_lines = list(filter(lambda line: line.startswith("import") or line.startswith("from"), self.notebook_code.split("\n")))
        self.import_augmented_code = "\n".join(import_lines) + "\n" + self.cell["source"]
        outputs = self.cell["outputs"]
        if len(outputs) == 0:
            self.output = ""
        elif "traceback" in outputs[0]:
            self.output = self.remove_ansi("\n".join(outputs[0]["traceback"]))
        else:
            self.output = outputs[0]["text"]
        self.reference_search_engine = ReferenceSearchEngine(self.parse_symbol_index(self.notebook_code))
        super().__init__()

    def remove_ansi(self, ansi_output: str) -> str:
        """
        Removes ANSI escape sequences
        """
        ansi_escape = re.compile(r'''
            \x1B  # ESC
            (?:   # 7-bit C1 Fe (except CSI)
                [@-Z\\-_]
            |     # or [ for CSI, followed by a control sequence
                \[
                [0-?]*  # Parameter bytes
                [ -/]*  # Intermediate bytes
                [@-~]   # Final byte
            )
        ''', re.VERBOSE)
        return ansi_escape.sub('', ansi_output)


    def analyze(self) -> str:
        content = f"""
        im getting this error, I would like to read the docs to fix it but i dont know which docs i should read. What module, class, and/or function should I retrieve information about. 

        Do not give me explanations, just reply with a list of matches in JSON format:
        ["example_module1.example_class1", "example_class2", "example_class3"."function1" ... ]

        <code>
        {self.import_augmented_code}
        </code> 

        <output>
        {self.output}
        </output> 
        """

        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": content}
            ]
        )
        openai_response = completion.choices[0].message
        openai_content = openai_response["content"]

        queries = json.loads(openai_content)
        #queries = ['pinecone', 'pinecone.Index', 'create_index']
        context = ""
        for query in queries:
            reference = self.reference_search_engine.search(query)
            if reference == "":
                continue 
            reference_context = f"""
{query} reference:
```
{reference}
```

            """
            context += reference_context

        return context

    def summarize_function(self, method_info) -> str:
        name = method_info["name"]
        docstring = method_info["docstring"]
        docstring_summary = ": " + docstring.split('\n')[0] if docstring else ""
        signature = method_info["signature"]
        signature_summary = name + "(" + ", ".join([f"[{param_name},{param_type}, {param_default}]" for param_name, param_type, param_default in signature]) + ")"
        return signature_summary + docstring_summary

    def parse_symbol_index(self, code):
        """
        Parses the code and returns a dictionary with the following keys:
        - imported_modules: list of imported modules
        - global_variables: dictionary of global variables and their values
        - defined_functions: dictionary of defined functions and their docstrings
        - defined_classes: dictionary of defined classes and their methods
        """
        # Parse the code using the ast module
        tree = ast.parse(code)

        # Define a custom AST visitor to collect function definitions, imported modules, and global variable assignments
        class FunctionInfoCollector(ast.NodeVisitor):

            def parse_args(self, args) -> str:
                # Extract information about the arguments
                arg_names = [arg.arg for arg in args.args]
                defaults = args.defaults
                num_defaults = len(defaults)
                num_args = len(arg_names)

                # Determine the required and optional arguments
                required_args = arg_names[:num_args - num_defaults]
                optional_args = arg_names[num_args - num_defaults:]

                # Construct the signature string
                signature_parts = []
                for arg_name in required_args:
                    signature_parts.append(arg_name)
                for i, arg_name in enumerate(optional_args):
                    default_value = ast.unparse(defaults[i])
                    signature_parts.append(f"{arg_name}={default_value}")

                # Join the signature parts to form the complete signature
                return ", ".join(signature_parts)

            def visit_Import(self, node):
                # Collect imported modules
                for alias in node.names:
                    imported_modules.append(alias.name)
                self.generic_visit(node)

            def visit_ImportFrom(self, node):
                # Collect imported modules
                imported_modules.append(node.module)
                self.generic_visit(node)

            def visit_Assign(self, node):
                # Collect global variable assignments
                if isinstance(node.targets[0], ast.Name):
                    variable_name = node.targets[0].id
                    # Ignore private variables (names starting with an underscore)
                    if not variable_name.startswith('_'):
                        global_variables[variable_name] = astunparse.unparse(node.value).strip()
                self.generic_visit(node)

            def visit_FunctionDef(self, node):
                # Collect defined functions and their docstrings
                function_name = node.name
                # Ignore private functions (names starting with an underscore)
                if not function_name.startswith('_'):                    
                    docstring = ast.get_docstring(node) if ast.get_docstring(node) else ""
                    signature = self.parse_args(node.args)
                    #signature_summary = function_name + "(" + ", ".join([f"[{param_name},{param_type}, {param_default}]" for param_name, param_type, param_default in signature]) + ")"
                    summary =  signature +"\n"+ docstring
                    defined_functions[function_name] = {
                        "name": function_name,
                        "docstring": docstring,
                        "signature": signature,
                        "summary": summary
                    }
                self.generic_visit(node)

            def visit_ClassDef(self, node):
                # Collect defined classes and their methods
                class_name = node.name
                # Ignore private classes (names starting with an underscore)
                if not class_name.startswith('_'):
                    class_methods = {}
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            method_name = item.name
                            # Ignore private methods (names starting with an underscore)
                            if not method_name.startswith('_') or method_name == "__init__":
                                signature = self.parse_args(item.args)
                                summary = signature + "\n" + docstring
                                class_methods[method_name] = {
                                    "docstring": docstring,
                                    "name": method_name, 
                                    "summary": summary
                                }
                    defined_classes[class_name] = class_methods
                self.generic_visit(node)

        # Use the custom AST visitor to collect defined functions, imported modules, and global variable assignments
        imported_modules = []
        global_variables = {}
        defined_functions = {}
        defined_classes = {}
        collector = FunctionInfoCollector()
        collector.visit(tree)

        # Load imported modules and retrieve their function signatures
        module_info = {}
        for module_name in imported_modules:
            try:
                module = __import__(module_name)
                functions = {}
                for name, obj in inspect.getmembers(module, inspect.isfunction):
                    # Ignore private functions (names starting with an underscore)
                    if not name.startswith('_'):
                        try:
                            signature = [(param_name, param.annotation.__name__ if hasattr(param.annotation, '__name__') and param.annotation != inspect.Parameter.empty else "", "required" if param.default is inspect.Parameter.empty else "") for param_name, param in inspect.signature(obj).parameters.items()]
                            # create a signature summary by converting into a string 
                            signature_summary = name + "(" + ", ".join([f"[{param_name},{param_type}, {param_default}]" for param_name, param_type, param_default in signature]) + ")"
                            docstring = inspect.getdoc(obj) if inspect.getdoc(obj) is not None else ""
                            functions[name] = {
                                "name": name,
                                "signature": signature,
                                "docstring": docstring,
                                "summary": signature_summary + "\n" + docstring
                            }
                        except ValueError:
                            # Skip functions for which a signature cannot be retrieved
                            pass

                classes = {}
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    # Ignore private classes (names starting with an underscore)
                    if not name.startswith('_'):
                        class_methods = {}
                        for method_name, method_obj in inspect.getmembers(obj, inspect.isfunction):
                            # Ignore private methods (names starting with an underscore)
                            if not method_name.startswith('_'):
                                try:
                                    signature = [(param_name, param.annotation.__name__ if hasattr(param.annotation, '__name__') and param.annotation != inspect.Parameter.empty else "", "required" if param.default is inspect.Parameter.empty else "") for param_name, param in inspect.signature(method_obj).parameters.items()]
                                    # create a signature summary by converting into a string 
                                    signature_summary = method_name + "(" + ", ".join([f"[{param_name},{param_type}, {param_default}]" for param_name, param_type, param_default in signature]) + ")"
                                    docstring = "\n\n" + inspect.getdoc(method_obj) if inspect.getdoc(method_obj) is not None else ""
                                    class_methods[method_name] = {
                                        "name": method_name,
                                        "signature": signature,
                                        "docstring": docstring,
                                        "summary": signature_summary + docstring
                                    }
                                except ValueError:
                                    # Skip methods for which a signature cannot be retrieved
                                    pass
                                
                        summary = ""
                        for _, method_info in class_methods.items():
                            summary += self.summarize_function(method_info) + "\n"

                        classes[name] = {
                            'name':  name,
                            'functions' : class_methods,
                            'summary' : summary
                        }

                summary = "\n"
                for _, function_info in functions.items():
                    summary += self.summarize_function(function_info) + "\n\n"

                module_info[module_name] = {
                    'name': module_name,
                    'functions': functions,
                    'classes': classes,
                    'summary': summary
                }

            except ImportError:
                print(f"Warning: Unable to import module '{module_name}'.")

        global_variables_str = '\n'.join([f'{key}={value}' for key, value in global_variables.items()])
        # Convert the module information, global variables, defined functions, and defined classes to a JSON array
        return {
            "modules": module_info,
            "variables": global_variables_str,
            "functions": defined_functions,
            "classes": defined_classes
        }

class SearchEngine(ABC):
    """
    Abstract class for search engine
    """

    def search(self, query) -> list[str]:
        """
        Search for query and return a list of results
        """
        
class ReferenceSearchEngine(SearchEngine):
    """
    Search engine for reference documentation crawled from PyPi modules code 
    """
    def __init__(self, symbols_index) -> None:
        self.symbol_index = symbols_index
        super().__init__()

    def search(self, query) -> list[str]:
        nodes = query.split('.')
        return self.lookup(self.symbol_index, nodes, None)
    
    def lookup(self, index, path, max_depth):
        """
        Lookup a path in a nested dictionary
        """
        if (not isinstance(index, dict) or len(path) == 0 or len(index) == 0 or max_depth == 0):
            return ""

        key = path[0]
        if len(path) == 1 and key in index:
            return index[key]["summary"]
        else:
            results = []
            for k, sub_index in index.items():
                depth_increase = 0 if k in ["variables", "functions", "classes", "modules"] else 1
                sub_max_depth = None if max_depth is None else max_depth - depth_increase
                if k == key:
                    results.append(self.lookup(sub_index, path[1:], 1))
                else:
                    results.append(self.lookup(sub_index, path, sub_max_depth))
            matches = list(filter(lambda match: len(match) > 0, results))
            if len(matches) > 0:
                return matches[0]
            else:
                return ""


class DocsSearchEngine(SearchEngine):
    """
    Search engine for documentation crawled from PyPi modules documentation
    """
    def search(self, query) -> list[str]:
        pass

if __name__ == '__main__':
    REQUEST = json.loads(REQUEST_JSON)
    static_analyzer = StaticAnalyzer(REQUEST)
    static_analysis = static_analyzer.analyze()
    debugger = VarReaderAnalyzer(REQUEST)
    debugger_analysis = debugger.analyze()
    print(f"{static_analysis}\n{debugger_analysis}") 
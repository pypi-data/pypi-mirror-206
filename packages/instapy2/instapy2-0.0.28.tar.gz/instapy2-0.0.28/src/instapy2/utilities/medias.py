from instagrapi import Client
from instagrapi.types import Media

class Medias:
    def __init__(self, session: Client):
        self.session = session

    
    def get_medias_for_hashtag(self, amount: int, hashtag: str, **kwargs) -> list[Media]:
        tab_key = kwargs['tab_key'] if 'tab_key' in kwargs.keys() else 'edge_hashtag_to_media'
        identifiers_to_skip = kwargs['identifiers_to_skip'] if 'identifiers_to_skip' in kwargs.keys() else []
            
        end_cursor = ''
        medias = []

        while len(medias) < amount:
            try:
                chunk, cursor = self.session.hashtag_medias_a1_chunk(name=hashtag, max_amount=amount, tab_key=tab_key, end_cursor=end_cursor)
                medias += [media for media in chunk if media.id not in identifiers_to_skip]
                end_cursor = cursor
            except:
                try:
                    chunk, cursor = self.session.hashtag_medias_v1_chunk(name=hashtag, max_amount=amount, tab_key=tab_key, max_id=end_cursor)
                    medias += [media for media in chunk if media.id not in identifiers_to_skip]
                    end_cursor = cursor
                except:
                    break

        return medias
    
    def get_medias_for_location(self, amount: int, location: int, **kwargs) -> list[Media]:
        tab_key = kwargs['tab_key'] if 'tab_key' in kwargs.keys() else 'edge_location_to_media'
        identifiers_to_skip = kwargs['identifiers_to_skip'] if 'identifiers_to_skip' in kwargs.keys() else []

        max_id = ''
        medias = []

        while len(medias) < amount:
            try:
                chunk, cursor = self.session.location_medias_a1_chunk(location_pk=location, max_amount=amount, tab_key=tab_key, max_id=max_id)
                medias += [media for media in chunk if media.id not in identifiers_to_skip]
                max_id = cursor
            except:
                try:
                    chunk, cursor = self.session.location_medias_v1_chunk(location_pk=location, max_amount=amount, tab_key=tab_key, max_id=max_id)
                    medias += [media for media in chunk if media.id not in identifiers_to_skip]
                    max_id = cursor
                except:
                    break

        return medias
    
    def get_medias_for_user(self, amount: int, username: str, **kwargs) -> list[Media] | None:
        identifiers_to_skip = kwargs['identifiers_to_skip'] if 'identifiers_to_skip' in kwargs.keys() else []
            
        end_cursor = ''
        medias = []

        try:
            user_id = self.session.user_id_from_username(username=username)
            user_id_int = int(user_id)
        except:
            user_id_int = None

        if user_id_int is None:
            return None
        else:
            while len(medias) < amount:
                try:
                    chunk, cursor = self.session.user_medias_paginated(user_id=user_id_int, amount=amount, end_cursor=end_cursor)
                    medias += [media for media in chunk if media.id not in identifiers_to_skip]
                    end_cursor = cursor
                except:
                    try:
                        chunk, cursor = self.session.user_medias_paginated_v1(user_id=user_id_int, amount=amount, end_cursor=end_cursor)
                        medias += [media for media in chunk if media.id not in identifiers_to_skip]
                        end_cursor = cursor
                    except:
                        break

            return medias
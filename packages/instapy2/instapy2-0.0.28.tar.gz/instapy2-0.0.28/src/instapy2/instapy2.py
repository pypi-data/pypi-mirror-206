from .utilities import LoggerConstants, Utility
from .types import CommentType, LikeType, PostType

from datetime import datetime
from os import getcwd, sep
from pathlib import Path
from random import choice, randint
from requests import get
from urllib.request import urlretrieve


class InstaPy2(Utility):
    def comment(self, amount: int, iterable: list[int | str | None], type: CommentType, **kwargs):
        # self.logger.error(message='THIS IS A WIP REWORK. PLEASE USE `MAIN`.')
        # exit(0)

        if 'do_after' in kwargs.keys():
            function = kwargs['do_after']()
        else:
            function = self.nop()

        match type:
            case CommentType.HASHTAG:
                for elem in iterable:
                    hashtag = str(elem)

                    identifiers = self.persistence.all_identifiers(table='medias_comments_hashtag')
                    medias = self.medias.get_medias_for_hashtag(amount=amount, hashtag=hashtag, identifiers_to_skip=identifiers)

                    for media in medias:
                        if not self.is_media_validated_for_interaction(media=media):
                            self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                        else:
                            self.logger.info(message=LoggerConstants.MEDIA_VALID)
                            if not self.persistence.identifier_exists(table='medias_comments_hashtag', identifier=media.id):
                                if not randint(a=0, b=100) <= self.comments.percentage:
                                    self.logger.error(message=LoggerConstants.PERCENTAGE_OUT_OF_BOUNDS)
                                else:
                                    try:
                                        commented = self.session.media_comment(media_id=media.id, text=choice(seq=self.comments.comments)) is not None
                                        if not commented:
                                            self.logger.error(message=LoggerConstants.MEDIA_COMMENT_FAIL)
                                        else:
                                            self.persistence.insert_identifier(table='medias_comments_hashtag', identifier=media.id, timestamp=datetime.now())
                                            self.logger.info(message=LoggerConstants.MEDIA_COMMENT_SUCCESS)
                                    except:
                                        self.logger.error(message=LoggerConstants.MEDIA_COMMENT_FAIL)
                            else:
                                pass
                        self.do_after(function=function)

    def like(self, amount: int, iterable: list[int | str | None], type: LikeType, **kwargs):
        # self.logger.error(message='THIS IS A WIP REWORK. PLEASE USE `MAIN`.')
        # exit(0)

        if 'do_after' in kwargs.keys():
            function = kwargs['do_after']()
        else:
            function = self.nop()

        match type:
            case LikeType.HASHTAG:
                for element in iterable:
                    hashtag = str(element)

                    identifiers = self.persistence.all_identifiers(table='medias_likes_hashtag')
                    medias = self.medias.get_medias_for_hashtag(amount=amount, hashtag=hashtag, identifiers_to_skip=identifiers)

                    for media in medias:
                        if not self.is_media_validated_for_interaction(media=media):
                            self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                        else:
                            self.logger.info(message=LoggerConstants.MEDIA_VALID)
                            if not self.persistence.identifier_exists(table='medias_likes_hashtag', identifier=media.id):
                                try:
                                    liked = self.session.media_like(media_id=media.id)
                                    if not liked:
                                        self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                    else:
                                        self.persistence.insert_identifier(table='medias_likes_hashtag', identifier=media.id, timestamp=datetime.now())
                                        self.logger.info(message=LoggerConstants.MEDIA_LIKE_SUCCESS)
                                except:
                                    self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                            else:
                                pass
                        self.do_after(function=function)
            case LikeType.LOCATION:
                for elem in iterable:
                    location = self.get_pk(query=input('Enter a location name (eg: Bondi Beach, New South Wales): ')) if elem is None else int(elem)

                    if location is None:
                        self.logger.error(message=f'An error occurred while scraping media for location: {location}.')
                    else:
                        identifiers = self.persistence.all_identifiers('medias_likes_location')
                        medias = self.medias.get_medias_for_location(amount=amount, location=location, identifiers_to_skip=identifiers)

                        for media in medias:
                            if not self.is_media_validated_for_interaction(media=media):
                                self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                            else:
                                self.logger.info(message=LoggerConstants.MEDIA_VALID)
                                if not self.persistence.identifier_exists(table='medias_likes_location', identifier=media.id):
                                    try:
                                        liked = self.session.media_like(media_id=media.id)
                                        if not liked:
                                            self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                        else:
                                            self.persistence.insert_identifier(table='medias_likes_location', identifier=media.id, timestamp=datetime.now())
                                            self.logger.info(message=LoggerConstants.MEDIA_LIKE_SUCCESS)
                                    except:
                                        self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                else:
                                    pass
                            self.do_after(function=function)
            case LikeType.USER:
                for elem in iterable:
                    username = str(elem)

                    identifiers = self.persistence.all_identifiers(table='medias_likes_user')
                    medias = self.medias.get_medias_for_user(amount=amount, username=username, identifiers_to_skip=identifiers)

                    if medias is None:
                        self.logger.error(message=f'An error occurred while scraping media for user: {username}.')
                    else:
                        for media in medias:
                            if not self.is_media_validated_for_interaction(media=media):
                                self.logger.error(message=LoggerConstants.MEDIA_INVALID)
                            else:
                                self.logger.info(message=LoggerConstants.MEDIA_VALID)
                                if not self.persistence.identifier_exists(table='medias_likes_user', identifier=media.id):
                                    try:
                                        liked = self.session.media_like(media_id=media.id)
                                        if not liked:
                                            self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                        else:
                                            self.persistence.insert_identifier(table='medias_likes_user', identifier=media.id, timestamp=datetime.now())
                                            self.logger.info(message=LoggerConstants.MEDIA_LIKE_SUCCESS)
                                    except:
                                        self.logger.error(message=LoggerConstants.MEDIA_LIKE_FAIL)
                                else:
                                    pass
                            self.do_after(function=function)

    def post(self, type: PostType, path: Path | None = None, caption: str = None, **kwargs):
        match type:
            case PostType.LOCAL:
                if path is None or caption is None:
                    self.logger.error(message='No image path or caption has been entered for the argument(s) \'path\' or \'caption\'.')
                else:
                    try:
                        self.session.photo_upload(path=path, caption=caption)
                    except:
                        self.logger.error(message='Failed to upload photo.')
            case PostType.PEXELS:
                if any(key not in ['api_key', 'caption', 'query'] for key in kwargs.keys()):
                    self.logger.error(message='No api_key, caption or query entered for argument(s) \'api_key\', \'caption\' or \'query\'.')
                else:
                    query = kwargs['query']
                    json_data = get(url=f'https://api.pexels.com/v1/search?query={query}&page=1&per_page=1', headers={'Authorization' : kwargs['api_key']}).json()

                    if 'photos' not in json_data:
                        self.logger.error(message='No photos could be found for the entered query.')
                    else:
                        photo = json_data['photos'][0]
                        # id = photo['id'] # save this using persistence
                        url = photo['src']['original']
                        file_path, _ = urlretrieve(url=url, filename=getcwd() + sep + 'files' + sep + 'image.png')
                        self.session.photo_upload(path=Path(file_path), caption=caption)
            case PostType.UNSPLASH:
                if any(key not in ['api_key', 'caption', 'query'] for key in kwargs.keys()):
                    self.logger.error(message='No api_key, caption or query entered for argument(s) \'api_key\', \'caption\' or \'query\'.')
                else:
                    query = kwargs['query']
                    json_data = get(url=f'https://api.unsplash.com/search/photos?query={query}&page=1&per_page=1', headers={'Authorization' : 'Client-ID ' + kwargs['api_key']}).json()

                    if 'results' not in json_data:
                        self.logger.error(message='No photos could be found for the entered query.')
                    else:
                        photo = json_data['results'][0]
                        # id = photo['id'] # save this using persistence
                        url = photo['urls']['regular']
                        file_path, _ = urlretrieve(url=url, filename=getcwd() + sep + 'files' + sep + 'image.png')
                        self.session.photo_upload(path=Path(file_path), caption=caption)

    def unfollow(self, amount: int):
        followers = self.session.user_followers(user_id=self.session.user_id, amount=amount)
        [self.session.user_unfollow(user_id=user_id) for user_id in followers.keys()]
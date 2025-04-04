from django.templatetags.static import static


DEFAULT_AGENCY_IMAGE_URL = static('images/default_agency.png')
DEFAULT_HEADER_IMAGE_URL = static('images/default_header.png')
DEFAULT_TRAVEL_IMAGE_URL = static('images/default_travel.png')
DEFAULT_THEME_IMAGE_URL = static('images/default_theme.png')
FORCED_IMAGE_FORMAT = 'WEBP'
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB
AGENCY_LIST_VIEW_TIMEOUT = 60 * 60 * 4  # 60s * 60m * 4h
AGENCY_DETAIL_VIEW_TIMEOUT = 60 * 60 * 4  # 60s * 60m * 4h
AGENCY_CATEGORY_VIEW_TIMEOUT = 60 * 60 * 4  # 60s * 60m * 4h
CATEGORY_DETAIL_VIEW_TIMEOUT = 60 * 60 * 4  # 60s * 60m * 4h
NEW_TRAVEL_DAYS = 10

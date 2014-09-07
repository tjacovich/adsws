SOLR_SEARCH_HANDLER = 'http://localhost:9000/solr/select'
SOLR_UPDATE_HANDLER = 'http://localhost:9000/solr/update'

EXTENSIONS = ['adsws.ext.menu',
              'adsws.ext.sqlalchemy',
              'adsws.ext.security',]

PACKAGES = ['adsws.modules.oauth2server',
            'adsws.api.solr']
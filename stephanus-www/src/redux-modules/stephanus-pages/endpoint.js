import { createEndpoint } from 'redux-endpoints';
import urlParse from 'url-parse';

const normalizeJson = json => (
  json.reduce((memo, page) => {
    memo[page.id] = page;
    return memo;
  }, {})
);

const endpoint = createEndpoint({
  name: 'stephanus-api',
  request: (url, options) => new Promise((resolve, reject) => {
    const parsedUrl = urlParse(url);
    parsedUrl.set('query', options.query);

    fetch(parsedUrl.toString())
      .then(resp => resp.json())
      .then(json => resolve(normalizeJson(json)));
  }),
  resolver: options => `${options.query.from}:${options.query.to}`,
  url: 'http://api.stephanuspages.com/pages',
});

export default endpoint;

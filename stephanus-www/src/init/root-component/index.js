import React from 'react';
import store from 'redux-store';
import { Provider } from 'react-redux';

import { App } from 'connected-components';

const root = () => (
  <Provider store={store}>
    <App />
  </Provider>
);

export default root;

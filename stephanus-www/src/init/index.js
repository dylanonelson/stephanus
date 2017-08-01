import React from 'react';
import ReactDOM from 'react-dom';

import root from './root-component';
import store from 'redux-store';
import { actionCreators } from 'redux-modules/stephanus-pages';

const renderApp = () => {
  ReactDOM.render(
    React.createElement(root),
    document.getElementById('root')
  );
};

document.addEventListener('DOMContentLoaded', renderApp)

store.dispatch(actionCreators.request({
  query: {
    from: '327a',
    to: '329a',
  },
}));

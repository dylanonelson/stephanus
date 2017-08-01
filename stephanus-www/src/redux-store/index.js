import createSagaMiddleware from 'redux-saga';
import { applyMiddleware, compose, createStore } from 'redux';

import initialState from './initialState';
import reducer from './reducer';
import { middleware as pagesMiddleware } from 'redux-modules/stephanus-pages';


const sagaMiddleware = createSagaMiddleware();

const middleware = applyMiddleware(
  pagesMiddleware,
  sagaMiddleware,
);

const composeEnhancers =
  window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose; // eslint-disable-line

export default createStore(reducer, initialState, composeEnhancers(middleware));

// sagaMiddleware.run(mySaga);

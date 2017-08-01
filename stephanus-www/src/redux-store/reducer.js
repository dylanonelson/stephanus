import { combineReducers } from 'redux';
import reduceReducers from 'reduce-reducers';

import stephanusApi from 'redux-modules/stephanus-pages';
import rootReducer from './root';

const compositeReducer = combineReducers(Object.assign({},
  stephanusApi,
));

export default reduceReducers(
  rootReducer,
  compositeReducer,
);

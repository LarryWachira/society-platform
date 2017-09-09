import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom';
import App from './components/App';
import Login from './components/Login'
import './static/css/style.css';

ReactDOM.render(
    <div>
        <BrowserRouter>
            <div>
                <Route exact path="/" component={App} />
                <Route exact path="/login" component={Login} />
            </div>
        </BrowserRouter>
    </div>, 
    document.getElementById('app')
);

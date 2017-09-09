import React, { Component } from 'react';
import gapi from 'gapi-client';
import '../static/css/signin.css';
import logo from '../static/images/andela-logo-blue.png';

class Login extends Component{
    render(){
        return (
            <div className="flex">
                <div id="container">
                    <div id="s-logo">
                        <img src={logo} alt="Logo" />
                    </div>
                    <div id="app-details">
                        <h1 className="title">Open platform</h1>
                        <p className="description">
                            A mini social networking platform that enables Andela societies to connect.
                        </p>
                    </div>
                    <div id="signin-button"></div>
                </div>
            </div>
        );
    }
}

export default Login;

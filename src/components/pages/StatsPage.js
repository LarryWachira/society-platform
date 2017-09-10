import React from  'react';
import {Link} from 'react-router-dom';

const StatsPage = props => {

        return (
            <div id="app-header" className="no-content">
            <div className="container">
                <Link to="/" id="logo">
                    <img src={props.logo} alt="Logo" />
                </Link>
                <div id="account-tools">
                    {props.accountAction}
                </div>
                
            </div>
        </div>
    );
}

export default StatsPage;

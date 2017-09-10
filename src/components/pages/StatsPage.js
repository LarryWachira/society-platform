import React from  'react';
import {Link} from 'react-router-dom';

const StatsPage = props => {

        return (
            <div id="app-header" className="no-content">
            <div className="container">
                <Link to="/" id="logo">
                    <img src={props.logo} alt="Logo" />
                    <span className="blue-text">Society Points</span>
                </Link>
                <div id="account-tools">
                    {props.accountAction}
                </div>
                <div id="page-content">
                    <div id="main-page-content">
                        <header id="page-header">
                            <h2 id="page-title">Stats</h2>
                        </header>
                        <div id="">
                            body
                        </div>
                    </div>
                    <aside id="side-content">
                        sidebar
                    </aside>
                </div>
            </div>
        </div>
    );
}

export default StatsPage;

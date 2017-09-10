import React from  'react';
import {Link} from 'react-router-dom';

const HomePage = props => {

        return (
            <div id="app-header" className="" style={{backgroundImage: `url(https://photos.smugmug.com/Archives/Kenya/Internal-Events/First-Access-6-Year-Anniversary/i-QsMqWTf/0/503e29b2/X3/First_Access_6_Year_Anniversary%20-1-X3.jpg)`}}>
            <div className="container">
                <Link to="/" id="logo">
                    <img src={props.logo} alt="Logo" />
                    <span>Society Points</span>
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
                        </div>
                    </div>
                    <aside id="side-content">
                        
                    </aside>
                </div>
            </div>
        </div>
    );
}

export default HomePage;

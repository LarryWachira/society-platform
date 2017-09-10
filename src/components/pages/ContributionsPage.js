import React from  'react';
import {Link} from 'react-router-dom';

const Contributions = props => {

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
                            <h2 id="page-title">Contributions</h2>
                        </header>
                        <div id="">
                            <table id="activities-table" className="contributions">
                                <thead>
                                    <th>Activity</th>
                                    <th className="center-text">No. of points</th>
                                    <th></th>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>
                                            <span className="activity-type">Attended hackathon</span>
                                            <p className="comment">
                                            Description. lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet 
                                            </p>
                                        </td>
                                        <td className="center-text">80</td>
                                        <td className="actions">
                                            <span className="action approved">
                                                <i className="fa fa-check"></i>
                                                <span className="action-text">Approved</span>
                                            </span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <span className="activity-type">Attended hackathon</span>
                                            <p className="comment">
                                            Description. lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet 
                                            </p>
                                        </td>
                                        <td className="center-text">80</td>
                                        <td className="actions">
                                            <span className="action pending">
                                                <i className="fa fa-circle-o"></i>
                                                <span className="action-text">Pending</span>
                                            </span>
                                        </td>
                                    </tr>
                                    
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <aside id="side-content">
                        
                    </aside>
                </div>
            </div>
        </div>
    );
}

export default Contributions;

import React from  'react';
import {Link} from 'react-router-dom';

const ActivityLogsPage = props => {

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
                            <h2 id="page-title">Logged activities</h2>
                        </header>
                        <div id="">
                            <table id="activities-table">
                                <thead>
                                    <th>Name</th>
                                    <th>Activity</th>
                                    <th className="center-text">No. of points</th>
                                    <th></th>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>John Paul Oyomtho</td>
                                        <td>
                                            <span className="activity-type">Attended hackathon</span>
                                            <p className="comment">
                                            Description. lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet 
                                            </p>
                                        </td>
                                        <td className="center-text">80</td>
                                        <td className="actions">
                                            <span className="action">
                                                <i className="fa fa-check"></i>
                                                <span className="action-text">Approve</span>
                                            </span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>John Paul Oyomtho</td>
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
                                        <td>John Paul Oyomtho</td>
                                        <td>
                                            <span className="activity-type">Attended hackathon</span>
                                            <p className="comment">
                                            Description. lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet lorem ipsum dolar siot amet 
                                            </p>
                                        </td>
                                        <td className="center-text">70</td>
                                        <td className="actions">
                                            <span className="action">
                                                <i className="fa fa-check"></i>
                                                <span className="action-text">Approve</span>
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

export default ActivityLogsPage;

import React from 'react';
import {Link} from 'react-router-dom';

const Sidebar = props => {
    return (
        <div id="sidebar-content">
            <Link to="/" className="navlink"><i className="fa fa-home"></i> Home</Link>
            <Link to="/contributions" className="navlink"><i className="fa fa-list-alt"></i> Contributions</Link>
            <Link to="/logged-activities" className="navlink"><i className="fa fa-list-alt"></i> Logged activities</Link>
            <Link to="/stats" className="navlink"><i className="fa fa-area-chart"></i> Stats</Link>
            <span className="navlink-title">Societies</span>
            <Link to="/society/" className="navlink"><i className="fa fa-group"></i> Invicticus</Link>
            <Link to="/society/" className="navlink"><i className="fa fa-group"></i> Phoenix</Link>
            <Link to="/society/" className="navlink"><i className="fa fa-group"></i> Istelle</Link>
            <Link to="/society/" className="navlink"><i className="fa fa-group"></i> Sparks</Link>
        </div>
    );
}

export default Sidebar;

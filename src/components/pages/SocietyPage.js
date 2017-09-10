import React from  'react';
import {Link} from 'react-router-dom';
import SocietyInfo from '../SocietyInfo';
import Score from '../Score';

const SocietyPage = props => {
    return (
        <div id="app-header">
            <div className="container">
                <Link to="/" id="logo">
                    <img src={props.logo} alt="Logo" />
                </Link>
                <div id="account-tools">
                    {props.accountAction}
                </div>
                <SocietyInfo name="Invicticus" 
                    statement="We are invicticus"
                    badge="http://via.placeholder.com/150x150" />

                <Score score="3,382"
                    showForm={props.showActivityForm} />
            </div>
        </div>
    );
};

export default SocietyPage;

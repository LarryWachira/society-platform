import React from  'react';
import {Link} from 'react-router-dom';
import SocietyInfo from '../SocietyInfo';
import Score from '../Score';

const SocietyPage = props => {
    return (
        <div id="app-header" style={{backgroundImage: `url(https://photos.smugmug.com/Archives/Kenya/Internal-Events/Andela-Kenya-Turns-2/i-n6gSgRB/1/53c1e45f/X3/AndelaKenya2ndAnniversary_10-X3.jpg)`}}>
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

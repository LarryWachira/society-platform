import React, { Component } from 'react';
import SocietyInfo from './components/SocietyInfo';
import Score from './components/Score';
import './static/css/page.css';
import logoWhite from './static/images/andela-logo-white.png';

class App extends Component {

    constructor(props){
        super(props);
        this.bindEvents();
    }

    bindEvents(){
        this.toggleLogout = this.toggleLogout.bind(this);
        this.resetUI = this.resetUI.bind(this);
        this.toggleSidebar = this.toggleSidebar.bind(this);
    }

    componentWillMount(){
        this.state = this.getInitialState();
    }

    getInitialState(){
        return {
            iconClicked: false
        };
    }

    toggleLogout(event){
        event.preventDefault();
        event.stopPropagation();

        this.setState(prevState => {
            return {
                showLogout: !prevState.showLogout
            }
        });
    }

    resetUI(event){
        this.setState(prevState => {
            return {
                showLogout: false,
                showSidebar: false
            }
        })
    }

    renderInLightbox(component = null){
        if (!component){
            return <div />
        }
        return (
            <div id="lightbox">
                <a href="" id="lightbox-close">
                    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" id="Layer_1" x="0px" y="0px" width="512px" height="512px" viewBox="0 0 512 512">
                        <polygon className="st0" points="340.2,160 255.8,244.3 171.8,160.4 160,172.2 244,256 160,339.9 171.8,351.6 255.8,267.8 340.2,352   352,340.3 267.6,256 352,171.8 "/>
                    </svg>
                </a>
                <div id="lightbox-content">
                    <div id="lightbox-header">
                        <span className="title">Edit your page</span>
                    </div>
                    <div id="lightbox-body">
                        {component}
                    </div>
                </div>
            </div>
        );
    }

    getSidebarClass(){
        if (!this.state.showSidebar){
            return "sidebar-collapsed";
        }

        return "";
    }

    toggleSidebar(event){
        event.preventDefault();
        event.stopPropagation();

        this.setState(prevState => {
            return {
                showSidebar: !prevState.showSidebar
            }
        });
    }

    render() {
        return (
                <div onClick={this.resetUI}>
                    <div id="content" className={this.getSidebarClass()}>
                    <aside id="sidebar">
                    </aside>
                    <div id="app-content">
                            {/* <a href="" id="menu-icon" onClick={this.toggleSidebar}>
                                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 139 139"><line className="st0" id="XMLID_6_" x1="26.5" x2="112.5" y1="46.3" y2="46.3"/><line className="st0" id="XMLID_9_" x1="26.5" x2="112.5" y1="92.7" y2="92.7"/><line className="st0" id="XMLID_8_" x1="26.5" x2="112.5" y1="69.5" y2="69.5"/></svg>
                            </a> */}
                            <div id="app-header">
                                <div className="container">
                                    <a href="" id="logo">
                                        <img src={logoWhite} alt="Logo" />
                                    </a>
                                    <div id="account-tools">
                                        <div id="account-icon" onClick={this.toggleLogout}>
                                            <img alt="Profile picture" src="http://via.placeholder.com/45x45" />
                                        </div>
                                        {this.state.showLogout? 
                                            <div id="account-actions">
                                                <a href="" className="account-action">Logout</a>
                                            </div>:
                                            <span />
                                            }
                                    </div>
                        
                                    <SocietyInfo name="Invicticus" 
                                        statement="We are invicticus"
                                        badge="http://via.placeholder.com/150x150" />
                        
                                    <Score score="3,382" />
                                </div>
                            </div>
                        
                            <main id="main-content">
                                <div className="container">
                                    <div id="tab-navigation">
                                        <a href="" className="tab active">Home</a>
                                        <a href="" className="tab">Stats</a>
                                        <a href="" className="tab">About</a>
                                    </div>
                                    <div className="row">
                                        <div className="left">dd</div>
                                        <div className="right">hdh</div>
                                        <div className="clearfix"></div>
                                    </div>
                                </div>
                            </main>
                    </div>
                    
                </div>
                
                {this.renderInLightbox()}
            </div>
    );
  }
}

export default App;
import React, { Component } from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import SocietyPage from './pages/SocietyPage';
import StatsPage from './pages/StatsPage';
import HomePage from './pages/HomePage';
import ActivityLogsPage from './pages/ActivityLogsPage';
import ContributionsPage from './pages/ContributionsPage';
import ActivityForm from './forms/ActivityForm';
import Sidebar from './Sidebar';
import '../static/css/font-awesome.min.css';
import '../static/css/page.css'; 
import whiteLogo from '../static/images/andela-logo-white.png';
import blueLogo from '../static/images/andela-logo-blue.png'; 

class App extends Component {

    constructor(props){
        super(props);
        this.bindEvents();
    }

    getDefaultState(){
        return {
            isLoggedIn: false,
            iconClicked: false,
            showSidebar: false,
            showActivityForm: false,
            newActivity: {
                name: '',
                comment: '',
                quantity: 1,
                isWorking: false
            }
        };
    }

    bindEvents(){
        this.toggleLogout = this.toggleLogout.bind(this);
        this.resetUI = this.resetUI.bind(this);
        this.toggleSidebar = this.toggleSidebar.bind(this);
        this.onActivityChange = this.onActivityChange.bind(this);
        this.closeLightbox = this.closeLightbox.bind(this);
        this.addActivity = this.addActivity.bind(this);
        this.showActivityForm = this.showActivityForm.bind(this);
        this.logout = this.logout.bind(this);
    }

    componentWillMount(){
        this.state = this.getDefaultState();
    }

    closeLightbox(){
        this.setState(prevState => {
            return {
                showActivityForm: false
            }
        });
    }

    addActivity(event){
        const formData = {
            name: this.state.newActivity.name,
            quantity: this.state.newActivity.quantity,
            comment: this.state.newActivity.comment
        }

        console.log(formData)
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

    renderInLightbox(title, component = null){
        if (!component){
            return <div />
        }
        return (
            <div id="lightbox">
                <a id="lightbox-close" onClick={this.closeLightbox}>
                    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" id="Layer_1" x="0px" y="0px" width="512px" height="512px" viewBox="0 0 512 512">
                        <polygon className="st0" points="340.2,160 255.8,244.3 171.8,160.4 160,172.2 244,256 160,339.9 171.8,351.6 255.8,267.8 340.2,352   352,340.3 267.6,256 352,171.8 "/>
                    </svg>
                </a>
                <div id="lightbox-content">
                    <div id="lightbox-header">
                        <span className="title">{title}</span>
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

    showActivityForm(){
        const {state} = this;
        state.showActivityForm = true;
        this.setState(state);
    }

    login(){

    }

    logout(){
        
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

    onActivityChange(event){
        let {state} = this;

        state.newActivity[event.target.name] = event.target.value;
        this.setState(state);
    }

    renderActivityForm(){
        if (!this.state.showActivityForm){
            return <span />;
        }
        
        return this.renderInLightbox("Log an activity", 
            <ActivityForm name={this.state.newActivity.name}
                comment={this.state.newActivity.description}
                quantity={this.state.newActivity.quantity}
                onChange={this.onActivityChange}
                close={this.closeLightbox}
                addActivity={this.addActivity}
                isWorking={this.state.newActivity.isWorking} />);
    }

    renderAccountAction(){
        if (this.state.isLoggedIn){
            return (
                <div>
                    <div id="account-icon" onClick={this.toggleLogout}>
                        <img alt="Profile" src="http://via.placeholder.com/45x45" />
                    </div>
                    {this.state.showLogout? 
                        <div id="account-actions">
                            <a href="" className="account-action">Logout</a>
                        </div>:
                        <span />
                        }
                </div>
            );
        }

        return (
            <a id="login-btn">Login</a>
        );
    }

    render() {
        return (
                <BrowserRouter>
                    <div>
                        <div id="content" 
                            className={this.getSidebarClass()}>
                        <aside id="sidebar">
                            <Route exact path="*" component={Sidebar} />
                        </aside>
                        <div id="app-content" onClick={this.resetUI}>
                            <a href="" id="menu-icon" onClick={this.toggleSidebar}>
                                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 139 139"><line className="st0" id="XMLID_6_" x1="26.5" x2="112.5" y1="46.3" y2="46.3"/><line className="st0" id="XMLID_9_" x1="26.5" x2="112.5" y1="92.7" y2="92.7"/><line className="st0" id="XMLID_8_" x1="26.5" x2="112.5" y1="69.5" y2="69.5"/></svg>
                            </a>
                                <div>
                                    <Route exact path="/" component={() => {
                                        return <HomePage logo={whiteLogo}
                                            accountAction={this.renderAccountAction()} />
                                    }} />
                                    <Route exact path="/contributions" component={() => {
                                        return <ContributionsPage logo={blueLogo}
                                            accountAction={this.renderAccountAction()} />
                                    }} />
                                    <Route exact path="/logged-activities" component={() => {
                                        return <ActivityLogsPage logo={blueLogo}
                                            accountAction={this.renderAccountAction()} />
                                    }} />
                                    <Route exact path="/society/" component={() => {
                                        return <SocietyPage logo={whiteLogo}
                                            accountAction={this.renderAccountAction()}
                                            logout={this.logout}
                                            login={this.login}
                                            showActivityForm={this.showActivityForm} /> 
                                    }} />
                                    <Route exact path="/stats" component={() => {
                                        return <StatsPage logo={blueLogo}
                                                    accountAction={this.renderAccountAction()} />
                                    }} />
                                </div>
                        </div>
                        
                    </div>
                    
                    {this.renderActivityForm()}
                </div>
            </BrowserRouter>
    );
  }
}

export default App;

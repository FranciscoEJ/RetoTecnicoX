import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Routes,
    Link
} from "react-router-dom";
import Home from './home';
import Case from './case';
const Webpages = () => {
    return (
        <Router>
            <Route exact path="/" component={Home} />
            <Route path="/:number_case" component={Case} />
        </Router>
    );
};
export default Webpages;
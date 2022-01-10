import React from 'react';
import {
    BrowserRouter,
    Switch,
    Route,
    Routes,
    Link
} from "react-router-dom";
import Home from './home';
import Case from './case';
const Webpages = () => {
    return (
        <BrowserRouter>
            <div>
                <Routes>
                    <Route exact path="/" component={Home} />
                    <Route path="/:number_case" component={Case} />
                </Routes>
            </div>
        </BrowserRouter>
    );
};
export default Webpages;
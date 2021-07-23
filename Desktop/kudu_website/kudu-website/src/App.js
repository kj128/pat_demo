import React, { Component } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

import Home from './components/Home';

import 'bootstrap/dist/css/bootstrap.css'; 
import 'bootstrap-icons/font/bootstrap-icons.css';

export default class App extends Component {
  render() {
    return (
      <div className='App'>
        <Home /> 

      </div>
    )
  }
}

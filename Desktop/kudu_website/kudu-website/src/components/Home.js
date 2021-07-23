import React, { Component } from 'react';

import Navbar from './Navbar';
import Carousel from './Carousel';
import Footer from './Footer';

export default class Home extends Component {
    render() {
        return (
            <div>
                <Navbar /> 

                <Carousel />

                <div class="container-fluid p-5 bg-dark transparent bg-gradient text-light ml-auto">

                    <h2 class="text-center">Who We Are</h2>
                    <br/>
                    <br/>

                
                    <div class="row">
                        <div class="col">
                            <div class="container-fluid">
                                <img src={process.env.PUBLIC_URL + "images/fields.jpg"} width="500px" height="500px"/>
                            </div>
                        </div>

                        <div class="col">
                            <div class="container-fluid justify-content-right">
                                <p class="h5">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
                                labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
                                esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
                                in culpa qui officia deserunt mollit anim id est laborum.</p>
                                <br />

                                <p class="h5">
                                Morbi leo urna molestie at elementum. In massa tempor nec feugiat nisl pretium. In iaculis nunc 
                                sed augue lacus viverra vitae congue eu. Mauris vitae ultricies leo integer. Vulputate odio ut enim 
                                blandit. Ac turpis egestas sed tempus. Orci phasellus egestas tellus rutrum tellus pellentesque eu 
                                tincidunt tortor. Ut porttitor leo a diam. Amet consectetur adipiscing elit duis tristique sollicitudin nibh. 
                                Imperdiet nulla malesuada pellentesque elit eget. Consequat semper viverra nam libero justo laoreet. Aliquam 
                                sem et tortor consequat. Tincidunt ornare massa eget egestas purus viverra accumsan in. Orci phasellus egestas 
                                tellus rutrum tellus pellentesque eu. Tempus egestas sed sed risus pretium. Sed blandit libero volutpat sed cras. 
                                Nulla at volutpat diam ut venenatis tellus in metus.
                                </p>
                            </div>
                        </div>
                    </div>

                </div>

                <Footer />

                
            </div>
        )
    }
}

import React, { Component } from 'react';
import 'bootstrap/js/dist/carousel';

import './Carousel.css';
// import img1 from '../public/images/biotech.png';

export default class Carousel extends Component {
    render() {
        return (
                <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src={process.env.PUBLIC_URL + "images/biotech.png"} class="d-block w-100" alt="..."/>
                        </div>

                        <div class="carousel-item">
                            <img src={process.env.PUBLIC_URL + "images/biotech2.jpg"} class="d-block w-100" alt="..."/>
                        </div>

                        <div class="carousel-item">
                        <img src={process.env.PUBLIC_URL + "images/crops.jpg"} class="d-block w-100" alt="..." />
                        </div>
                    </div>

                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>

                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
                
                </div>
        )
    }
}

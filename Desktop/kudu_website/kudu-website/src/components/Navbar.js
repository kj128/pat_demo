import React, { Component } from 'react'

export default class Navbar extends Component {
    render() {
        return (
            <div>

                <nav class="navbar navbar-expand-lg navbar-light bg-light p-4">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">Kudu Biotech</a>

                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="toggleSupportedContent">
                            <ul class="navbar-nav ms-auto text-center">
                                <li class="nav-item">
                                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">What We Do</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">Projects</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">Experience</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        )
    }
}

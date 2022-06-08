import React, { Component } from 'react';
import projectn from '../Unkomliziert'

class MyWorkTime extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.state = { projectName: '' };
    }

    handleChange = (e) => {
        this.setState({ projectName: e.target.value });
    }

    render() {
        const projectName = this.state.projectName;
        return (
            <div>

            </div>

        );
    }
}

export default MyWorkTime;
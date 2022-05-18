import React, { Component } from 'react';
import BoilingVerdict from './exampl'

class Calculator extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.state = { temperature: '' };
    }

    handleChange(e) {
        this.setState({ temperature: e.target.value });
    }

    render() {
        const temperature = this.state.temperature;
        return (
            <fieldset>
                <legend>Enter the name of the project you´re looking for: </legend>
                <input
                    value={temperature}
                    onChange={this.handleChange} />
                <BoilingVerdict
                    celsius={(temperature)} />
            </fieldset>
        );
    }
}

export default Calculator;
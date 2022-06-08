import React, { Component } from 'react';
import BoilingVerdict from './exampl'
import BasicSelect from '../dropdown';
import { FormControl } from '@mui/material';
import { FormHelperText } from '@mui/material';
import { Input } from '@mui/material';
import { InputLabel } from '@mui/material';
import { Select } from '@mui/material';
import { MenuItem } from '@mui/material';
import DropDown from './dropDownTrial';
import { Box } from '@mui/material';
import ProjectSelection from './ProjectSelections';
import { Button } from '@mui/material';

class ProjectTimeOverview extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.state = {
            temperature: '',
            value: '',
        };
    }

    handleChange(e) {
        this.setState({ temperature: 'Neues Projekt' },
            function () {
                console.log('HandleChange', this.state.temperature)
            });
    }


    render() {
        const temperature = this.state.temperature;
        return (
            <div>
                <fieldset>
                    <legend>You have selected: </legend>
                    <BoilingVerdict
                        celsius={(temperature)} />
                </fieldset>
            </div>
        );
    }
}

export default ProjectTimeOverview;
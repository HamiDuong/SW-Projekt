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
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Project from '../../API/ProjectBO';
import { Button } from '@mui/material';
import IndividualTimeEntry from './IndividualTimeEntry';


class IndividualTime extends Component {
    constructor(props) {
        super(props);
        this.handleTempChange = this.handleTempChange.bind(this);
        this.handleAgeChange = this.handleAgeChange.bind(this);
        this.state = {
            temperature: '',
            age: '',
            project: ''
        };
    }

    handleTempChange(e) {
        this.setState({ temperature: e.target.value });
    }

    handleAgeChange(e) {
        this.setState({ age: e.target.value });
    }


    render() {
        const temperature = this.state.temperature;
        const age = this.state.age;
        return (
            <div>
                <div>
                    <Box sx={{ margin: 2 }}>
                        <FormControl variant="standard" sx={{ m: 1, minWidth: 160 }}>

                            <InputLabel>Selet your project</InputLabel>
                            <Select
                                labelId="demo-simple-select-helper-label"
                                id="demo-simple-select-helper"
                                value={age}
                                label="Age"
                                onChange={this.handleTempChange}>
                                <MenuItem value={'project A'}>Project A</MenuItem>
                                <MenuItem value={'project B'}>Project B</MenuItem>
                                <MenuItem value={'project C'}>Project C</MenuItem>
                            </Select>
                        </FormControl>
                    </Box>
                </div>
                <fieldset>
                    <legend>You have selected: </legend>
                    <BoilingVerdict
                        celsius={(temperature)} />
                </fieldset>
                <IndividualTimeEntry />
            </div>
        );
    }
}

export default IndividualTime;
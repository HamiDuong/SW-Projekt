import React, { Component } from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { InputLabel } from '@mui/material';
import { Button } from '@mui/material';
import { Box } from '@mui/system';
import BoilingVerdict from './OverTimeEntry';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

class ProjectSelection extends Component {
    constructor(props) {
        super(props);
        this.state = {
            project: '',
            projects: [],
            temperature: '',
            project_name: '',
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.setState({ temperature: e.target.value },
            function () {
                console.log('HandleChange', this.state.temperature)
            });
    }


    getAllProjects = () => {
        WorkTimeAppAPI.getAPI().getAllProjects().then(projectBO =>
            this.setState({
                projects: [projectBO],
            }, function () {
                console.log('2', this.state.projects)
            }))
    }

    componentDidMount() {
        this.getAllProjects()
    }

    somefunc() {
        const projects = this.state.projects
        return (
            <Select onChange={this.handleChange}>
                {projects.map(project =>
                    project.map(elem => <MenuItem value={elem.name} >{elem.name}</MenuItem>)

                )}
            </Select>
        )
    }

    render() {
        const projects = this.state.projects
        const temperature = this.state.temperature
        return (
            <Box>
                {/* <Select onChange={this.handleChange}>
                    {projects.map(project =>
                        project.map(elem => <MenuItem value={elem.name} >{elem.name}</MenuItem>)

                    )}
                </Select> */}
                {this.somefunc()}
                <fieldset>
                    <legend>You have selected: </legend>
                    <BoilingVerdict
                        celsius={(temperature)} />
                </fieldset>
            </Box>
        );
    }
}

export default ProjectSelection;

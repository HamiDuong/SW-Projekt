import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import TableCell from '@mui/material/TableCell';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';


class ActivityBookingEntry extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            user: '',
            userName: '',
            projectDuration: '',
        })
    }

    getProjectsForUser = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    componentDidMount() {
        this.getProjectsForUser(3, 1)
        this.getUserById(this.props.us_id)
        this.getProjectDuration(1)
    }

    getUserById(id) {
        WorkTimeAppAPI.getAPI().getUserById(id).then(userBO =>
            this.setState({
                user: userBO,
                userName: userBO[0].first_name
            }, function () {
                console.log('Hier ist der User: ', this.state.user)
            }))
    }


    getProjectDuration = (project_id) => {
        WorkTimeAppAPI.getAPI().getProjectDurationInDays(project_id).then(projectDurationBO =>
            this.setState({
                projectDuration: projectDurationBO
            }, function () {
                console.log('Hier ist der User: ', this.state.projectDuration)
            }))
    }

    render() {
        return (
            <Box>
                <Paper sx={{ width: '100%' }}>
                    <TableCell width={150}></TableCell>
                    <TableCell width={300}>{this.state.time}</TableCell>
                    <TableCell width={350}>{this.state.userName}</TableCell>
                    <TableCell width={350}>{this.props.current_c}</TableCell>
                    <TableCell width={350}>{this.props.capacity}</TableCell>
                    <TableCell width={200}>{this.state.projectDuration}</TableCell>
                </Paper>
            </Box>


        );
    }
}

export default ActivityBookingEntry;
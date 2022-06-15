import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Collapse from '@mui/material/Collapse';
import Box from '@mui/material/Box';
import Work from '@mui/icons-material/Work';
import { TableContainer } from '@mui/material';
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
        this.getProjectsForUser(this.props.act_id, this.props.us_id)
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
            <Box sx={{ margin: 1.5, justifyContent: 'space-evenly' }}>
                <Paper sx={{ width: '100%' }}>
                    <Table>
                        <TableBody>
                            <TableCell width='90'>{this.state.time}</TableCell>
                            <TableCell width='90'>{this.state.userName}</TableCell>
                            <TableCell width='90'>{this.props.current_c}</TableCell>
                            <TableCell width='90'>{this.props.capacity}</TableCell>
                            <TableCell width='90'>{this.state.projectDuration}</TableCell>
                        </TableBody>
                    </Table>
                </Paper>
            </Box>


        );
    }
}

export default ActivityBookingEntry;
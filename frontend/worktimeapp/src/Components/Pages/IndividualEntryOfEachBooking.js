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


class IndividualEntriesOfEachBooking extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            user_id: '',
            act_id: '',
            time: '',
            user: '',
            userName: '',
        })
    }

    getBookedTimeForUserOfAnActivity = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(time =>
            this.setState({
                time: time
            }, function () {
                console.log('Time:', this.state.time)
            }))
    }

    componentDidMount() {
        this.getBookedTimeForUserOfAnActivity(this.props.act_id, this.props.us_id)
        this.getUserById(this.props.us_id)
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

    render() {
        return (
            <Box sx={{ margin: 1.5 }}>
                <Paper sx={{ width: '700px' }}>
                    <Table>
                        <TableBody>
                            <TableCell width='70'>{this.state.time}</TableCell>
                            <TableCell width='70'>{this.props.current_c}</TableCell>
                            <TableCell width='70'>{this.props.capacity}</TableCell>
                        </TableBody>
                    </Table>
                </Paper>
            </Box>


        );
    }
}

export default IndividualEntriesOfEachBooking;
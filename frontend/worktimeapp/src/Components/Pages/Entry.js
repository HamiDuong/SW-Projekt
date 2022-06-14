import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Collapse from '@mui/material/Collapse';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import ActivityBookingEntry from './EntryOfEachBooking';
import { Grid, TableContainer } from '@mui/material';


class Entry extends Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this)
        this.state = ({
            activity: '',
            name: '',
            capacity: '',
            current_capacity: '',
            activities: '',
            members: '',
            userIds: [],
            open: false,

        })
    }

    getActivity(id) {
        WorkTimeAppAPI.getAPI().getActivityById(id).then(activityBO =>
            this.setState({
                activity: activityBO[0],
                name: activityBO[0].name,
                capacity: activityBO[0].capacity,
                current_capacity: activityBO[0].current_capacity
            }, function () {
                console.log('??', this.state.name)
            }))
    }

    componentDidMount() {
        this.getActivity(this.props.value)
        this.getProjectUser(1)
    }



    getProjectUser(projectId) {
        WorkTimeAppAPI.getAPI().getMembersByProjectId(projectId).then((member) =>
            this.setState({
                members: [...this.state.members, member[this.state.members.length]],
                userIds: [...this.state.userIds, member[this.state.members.length].user_id]
            }, function () {
                for (var i = 0; i < this.state.members.length; i++) {
                    console.log('!!', this.state.userIds)
                }
            }))
    }

    handleClick() {
        this.setState({
            open: !this.state.open,
        }, console.log('click'))
    }

    render() {
        const open = this.state.open
        const setOpen = this.state.setOpen
        return (
            <div>
                <Box
                    style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center'
                    }}>
                    <TableContainer>
                        <Table stickyHeader aria-label="sticky table">
                            <TableBody>
                                <Box
                                    style={{
                                        display: 'flex',
                                        alignItems: 'center',
                                        justifyContent: 'left'
                                    }}>

                                    <IconButton aria-label="expand row"
                                        size="small"
                                        onClick={this.handleClick}>
                                        {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                                    </IconButton>
                                    <TableRow>{this.state.name}</TableRow>
                                </Box>
                            </TableBody>
                        </Table>
                    </TableContainer>

                </Box>

                <Collapse in={open} timeout="auto" unmountOnExit>
                    <TableContainer style={{
                        display: 'flex',
                        justifyContent: 'center'
                    }}>
                        <Table sx={{ width: '75%' }}>
                            <TableHead>
                                <Box style={{
                                    display: 'flex'
                                }} sx={{ gap: 8 }}>
                                    <TableRow>Booked times</TableRow>
                                    <TableRow>Employees</TableRow>
                                    <TableRow>Planed capacity</TableRow>
                                    <TableRow >Current capacity</TableRow>
                                </Box>
                            </TableHead>
                            <Grid>
                                <TableBody>

                                    {this.state.userIds.map(element => {
                                        return (
                                            <ActivityBookingEntry act_id={this.props.value} us_id={element} capacity={this.state.capacity} current_c={this.state.current_capacity} />)
                                    })}

                                </TableBody>
                            </Grid>
                        </Table>
                    </TableContainer>
                </Collapse>
            </div >
        );
    }
}

export default Entry;


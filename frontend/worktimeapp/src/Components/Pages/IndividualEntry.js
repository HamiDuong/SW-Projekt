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
import { Grid, TableContainer } from '@mui/material';
import IndividualEntriesOfEachBooking from './IndividualEntryOfEachBooking';
import ScheduleIcon from '@mui/icons-material/Schedule';
import Divider from '@mui/material/Divider';
import ListAltIcon from '@mui/icons-material/ListAlt';
import TaskAltIcon from '@mui/icons-material/TaskAlt';


class IndividualEntry extends Component {
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
            userId: 1,
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
        this.getUser(this.state.userId)
    }



    getUser(id) {
        WorkTimeAppAPI.getAPI().getUserById(id).then(userBO => {
            this.setState({
                user: userBO
            }, function () {
                console.log('this is the user: ', userBO)
            })
        })
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
                <Box>
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
                            <Table sx={{ width: '70%' }}  >
                                <TableHead>

                                    <Box
                                        sx={{
                                            width: '100%',
                                            display: 'inline-flex',
                                            alignItems: 'center',
                                            justifyContent: 'space-evenly',
                                            border: (theme) => `1px solid ${theme.palette.divider}`,

                                            bgcolor: 'background.paper',
                                            color: 'text.secondary',
                                            '& svg': {
                                                m: 1.5,
                                            },
                                            '& hr': {
                                                mx: 1,
                                            },

                                        }}
                                    >
                                        <TaskAltIcon />
                                        <TableRow >Booked times</TableRow>
                                        <Divider orientation="vertical" flexItem />
                                        <ScheduleIcon size={'small'} />
                                        <TableRow>Planed project capacity</TableRow>
                                        <Divider orientation="vertical" flexItem />
                                        <ListAltIcon size={'small'} />
                                        <TableRow>Current capacity</TableRow>
                                    </Box>
                                </TableHead>

                                <TableBody>

                                    <IndividualEntriesOfEachBooking act_id={this.props.value} us_id={this.state.userId} capacity={this.state.capacity} current_c={this.state.current_capacity} />
                                </TableBody>




                            </Table>
                        </TableContainer>
                    </Collapse>
                </Box>
            </div >
        );
    }
}

export default IndividualEntry;
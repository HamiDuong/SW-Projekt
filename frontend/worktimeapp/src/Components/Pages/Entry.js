import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Collapse from '@mui/material/Collapse';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import ActivityBookingEntry from './EntryOfEachBooking'
import ScheduleIcon from '@mui/icons-material/Schedule';
import Divider from '@mui/material/Divider';
import ListAltIcon from '@mui/icons-material/ListAlt';
import TaskAltIcon from '@mui/icons-material/TaskAlt';
import { TableContainer, TableCell } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import MoreTimeIcon from '@mui/icons-material/MoreTime';


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
            projectId: this.props.projectId,
            projectDuration: '',
            userCapacity: [],

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
                console.log(this.state.name, activityBO[0].capacity)
            }))
    }

    componentDidMount() {
        this.getActivity(this.props.value)
        this.getProjectUser(this.props.projectId)
        this.getProjectDuration(this.props.projectId)
    }



    getProjectUser(projectId) {
        WorkTimeAppAPI.getAPI().getMembersByProjectId(projectId).then((member) => {
            console.log('was kommt eigentlich an?', member)
            if (member.length <= 0) {
                console.log('Weniger als 0')
                this.setState({
                    members: [0],
                    userIds: [0]
                })
            }
            else {
                this.setState({
                    members: member,
                }, function () {
                    console.log(this.state.members, 'Callback Function in Entry.js', this.state.userIds)
                }); this.getUserIds();
                this.getPlanedCapacitiesForUser()

            }
        }
        )
    }

    getUserIds() {
        let members = this.state.members
        let liste = []
        members.map(element =>
            liste.push(element.getUserId()),
            console.log('Hier ist die Liste', liste))
        this.setState({
            userIds: [...this.state.userIds, ...liste]
        }, function () {
            console.log('2. Callbackfunction', this.state.userIds)
        })
    }

    getPlanedCapacitiesForUser() {
        let members = this.state.members
        let listeZwei = []
        members.map(element =>
            listeZwei.push(element.getCapacity()),
            console.log('Hier ist die Liste', listeZwei))
        this.setState({
            userCapacity: [...this.state.userCapacity, ...listeZwei]
        }, function () {
            console.log('23458. Callbackfunction', this.state.userCapacity)
        })
    }

    getProjectDuration = (project_id) => {
        WorkTimeAppAPI.getAPI().getProjectDurationInDays(project_id).then(projectDurationBO =>
            this.setState({
                projectDuration: projectDurationBO
            }, function () {
                console.log('Hier ist der die Duration: ', this.state.projectDuration)
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

                        <Table style={{ marginLeft: '250px' }}>
                            <TableHead>
                                <Box sx={{
                                    marginTop: '5',
                                    width: '70%',
                                    display: 'inline-flex',
                                    alignItems: 'center',
                                    justifyContent: 'space-between',
                                    border: (theme) => `1px solid ${theme.palette.divider}`,
                                    color: 'text.secondary',
                                    '& svg': {
                                        m: 2,
                                    },
                                    '& hr': {
                                        mx: 1,
                                    },

                                }}>
                                    <Box sx={{
                                        width: '20%',
                                        display: 'inline-flex',
                                        alignItems: 'center',
                                        justifyContent: 'space-evenly'
                                    }}
                                    >
                                        <MoreTimeIcon />
                                        <TableRow >Project duration (in days) </TableRow>
                                        <TableRow>{this.state.projectDuration}</TableRow>
                                    </Box>
                                    <Box sx={{
                                        width: '20%',
                                        display: 'inline-flex',
                                        alignItems: 'center',
                                        justifyContent: 'space-evenly'
                                    }}>
                                        <ScheduleIcon size={'small'} />
                                        <TableRow>Planed capacity</TableRow>
                                        <TableRow>{this.state.capacity}</TableRow>
                                    </Box>
                                    <Box sx={{
                                        width: '20%',
                                        display: 'inline-flex',
                                        alignItems: 'center',
                                        justifyContent: 'space-evenly'
                                    }}>
                                        <ScheduleIcon size={'small'} />
                                        <TableRow>Total Booked Time</TableRow>
                                        <TableRow>{this.state.current_capacity}</TableRow>
                                    </Box>

                                </Box>
                            </TableHead>


                        </Table>


                        <TableContainer style={{
                            display: 'flex',
                            justifyContent: 'center'
                        }}>

                            <Table sx={{ width: '75%' }}>

                                <TableHead>
                                    <Box sx={{
                                        marginTop: '5',
                                        width: '100%',
                                        display: 'inline-flex',
                                        alignItems: 'center',
                                        justifyContent: 'space-evenly',
                                        border: (theme) => `1px solid ${theme.palette.divider}`,
                                        bgcolor: 'background.paper',
                                        color: 'text.secondary',
                                        '& svg': {
                                            m: 2,
                                        },
                                        '& hr': {
                                            mx: 1,
                                        },

                                    }}><ListAltIcon size={'small'} />
                                        <TableRow>Booked capacity</TableRow>
                                        <Divider orientation="vertical" flexItem />
                                        <PersonIcon />
                                        <TableRow>Employees</TableRow>
                                        <Divider orientation="vertical" flexItem />
                                        <TaskAltIcon />
                                        <TableRow >Planed capacity of employee</TableRow>

                                    </Box>
                                </TableHead>

                                <TableBody>

                                    {this.state.userIds.map((element, index) => {
                                        console.log(element, 'Ist das hier eine UserId?')
                                        return (
                                            <ActivityBookingEntry act_id={this.props.value} us_id={element} capacity={this.state.capacity} current_c={this.state.current_capacity} projectId={this.state.projectId}
                                                user_capa={this.state.userCapacity[index]} />)
                                    })}

                                </TableBody>

                            </Table>
                        </TableContainer>
                    </Collapse>
                </Box>
            </div >
        );
    }
}

export default Entry;
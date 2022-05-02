import React from 'react';
import MenuIcon from '@mui/icons-material/Menu';
import CloseIcon from '@mui/icons-material/Close';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PostAddIcon from '@mui/icons-material/PostAdd';
import PostAdd from '@mui/icons-material/PostAdd';
import TaskIcon from '@mui/icons-material/Task';
import WorkIcon from '@mui/icons-material/Work';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import AccessTimeFilledIcon from '@mui/icons-material/AccessTimeFilled';

export const SideBarData = [
    {
        title: 'MyProfile',
        path: '/myprofile',
        icon: <AccountCircleIcon/>,
        className : 'nav-text'
    },
    {
        title: 'CreateProjects',
        path: '/createprojects',
        icon: <TaskIcon/>,
        className : 'nav-text'
    },
    {
        title: 'MyWorkTime',
        path: '/myworktime',
        icon: <WorkIcon/>,
        className : 'nav-text'
    },
    {
        title: 'MyBookings',
        path: '/mybookings',
        icon: <PostAddIcon/>,
        className : 'nav-text'
    },
    {
        title: 'TimeIntervalBookings',
        path: '/timeintervalbookings',
        icon: <AccessTimeIcon/>,
        className : 'nav-text'
    },
    {
        title: 'EventBookings',
        path: '/eventbookings',
        icon: <AccessTimeFilledIcon/>,
        className : 'nav-text'
    },

    
]
import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import MenuIcon from '@mui/icons-material/Menu';
import CloseIcon from '@mui/icons-material/Close';
import {SideBarData} from './SideBarData';
import './NavBarCSS.css';

function NavBar () {
    //setSidebar aktualisert den currentValue
    const [sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)

    return(
        <>
            <div className='navbar'>
                <Link to='#' className='menu-bars'>
                   <MenuIcon onClick={showSidebar}/> 
                </Link>
            </div>
            <nav className={sidebar ? 'nav-menu active' : 'nav-menu' }>
                <ul className='nav-menu-items' onClick={showSidebar}  >
                    <li className='navbar-toggle'>
                        <Link to='#' className='menu-bars'>
                            <CloseIcon/>
                        </Link>
                    </li>
                    {SideBarData.map((item,index) => {
                        return(
                            <li key={index} className= {item.className}>
                                <Link to={item.path}>
                                    {item.icon}
                                    <span>
                                        {item.title}
                                    </span>
                                </Link>
                            </li>
                        )
                    })}
                </ul>
            </nav>
        </>
    )
}

export default NavBar;
import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import MenuIcon from '@mui/icons-material/Menu';
import CloseIcon from '@mui/icons-material/Close';
import {SideBarData} from './SideBarData';
import './NavBarCSS.css';
import { Typography } from '@mui/material';
import Search from '@mui/icons-material/Search';
import SearchIcon from '@mui/icons-material/Search';

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */
//Die Funktion NavBar zeigt eine Navigationleiste da, diese zeigt die einzelnen Pages und
//die den Namen unserer Applikation. 
function NavBar () {
    //setSidebar aktualisert den currentValue, useState wird false gesetzt, damit es noch nicht anzeigen tut 
    const [sidebar, setSidebar] = useState(false)

    //showSidebar wird die Menüleiste anzeigen. Es wird ein ArrowFunction gesetzt.
    //Es updated das Gegenteil von dem Wert, kann man sich wie ein toggle vorstellen, welches immer umschalten tut.
    const showSidebar = () => setSidebar(!sidebar)

    return(
        <>
        {/* Wir setzten classNames, da es später viel leichter ist diese zu gestalten mit CSS */}
            <div className='navbar'>
                {/*Der Pfad wird sehr simpel gehalten, Link dient für die Verlinkung von Style Sheet*/}
                <Link to='#' className='menu-bars'>
                    {/** hier wird showSidebar angewendet, wenn man auf den Icon klickt zeigt es die Menüleiste*/}
                   <MenuIcon onClick={showSidebar}/> 
                </Link>
                <Typography
                    className='navbar-headline'>
                    WorkTimeApp 
                </Typography>
                
            </div>
            {/* Hier wird nachgefragt, ob der Sidebar aktiv ist oder nicht. 
            Wenn es stimmt (TRUE) somit ändert sich das Stil und wenn nicht (FALSE) ist es wieder ein ganz anderer Stil*/}
            <nav style={{zIndex: 50}} className={sidebar ? 'nav-menu active' : 'nav-menu' }>
                <ul className='nav-menu-items' onClick={showSidebar}  >
                    <li className='navbar-toggle'>
                        <Link to='#' className='menu-bars'>
                            <CloseIcon/>
                        </Link>
                    </li>
                    {/**Hier rufen wir die SideBarData-Datei auf und setzten ein Platzhalter (item) */}
                    {SideBarData.map((item,index) => {
                        return(
                            //Wenn der ensprechender key und className stimmt, dann führt es folgendes aus
                            //Somit kann ich die Menüleiste beliebig oft ändern mit wenig auffand
                            <li key={index} className= {item.className}>
                                {/* Es verwendet den Pfand, welches wir in der SideBarData vordefiniert haben*/}
                                <Link to={item.path}>
                                    {/* Verwendet alle Icons, die von mir vordefiniert wurden und auch den Title */}
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
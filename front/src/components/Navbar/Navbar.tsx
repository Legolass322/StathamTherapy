import type {FC} from 'react'
import {memo, useMemo} from 'react'
import {useLocation, useNavigate} from 'react-router-dom'

import {TabItem, type TabItemProps} from './components/TabItem'

const NavbarInner: FC = () => {
  const navigate = useNavigate()
  const {pathname} = useLocation()

  const tabs: TabItemProps[] = useMemo(() => {
    return [
      {
        text: 'Profile',
        active: pathname.startsWith('/profile'),
        onClick: () => {
          navigate('/profile')
        },
      },
      {
        text: 'Statham',
        active: pathname.startsWith('/browse'),
        onClick: () => {
          navigate('/browse')
        },
      },
    ]
  }, [navigate, pathname])

  return (
    <div className="w-[96px] bg-slate-900">
      <ul className="mt-2 flex flex-col items-center px-2">
        {tabs.map((tab, i) => (
          <li key={i}>
            <TabItem {...tab} />
          </li>
        ))}
      </ul>
    </div>
  )
}

export const Navbar = memo(NavbarInner)

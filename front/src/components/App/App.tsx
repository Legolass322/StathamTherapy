import type {FC} from 'react'

import {AppRoutes} from '../../pages'
import {Navbar} from '../Navbar'

export const App: FC = () => {
  return (
    <div className="flex h-screen">
      <Navbar />
      <AppRoutes />
    </div>
  )
}

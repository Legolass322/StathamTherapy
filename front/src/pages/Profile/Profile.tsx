import type {FC} from 'react'
import {memo} from 'react'

const ProfileInner: FC = () => {
  return <div className="text-3xl font-bold underline text-center">Profile</div>
}

export const Profile = memo(ProfileInner)

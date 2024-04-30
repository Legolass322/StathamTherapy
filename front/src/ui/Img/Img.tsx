import {useMemo, type FC, memo} from 'react'

type ImgProps = {
  src: string
  width?: string | number
  height?: string | number
  className?: string
}

const ImgComponent: FC<ImgProps> = ({src, width, height, className}) => {
  const srcProp = useMemo(() => '/static/img/' + src, [src])
  const widthProp = useMemo(() => (typeof width === 'number' ? width + 'px' : width), [width])
  const heightProp = useMemo(() => (typeof height === 'number' ? height + 'px' : height), [height])
  return <img alt="img" className={className} src={srcProp} width={widthProp} height={heightProp} />
}

export const Img = memo(ImgComponent)

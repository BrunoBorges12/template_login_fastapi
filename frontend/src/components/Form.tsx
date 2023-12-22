'use client'
import { Button, Input, Switch } from '@nextui-org/react'
import React, { useState } from 'react'
import { FaEye } from 'react-icons/fa'
export const Form = () => {
    const [isVisible, setIsVisible] = useState(false)
    const [signIn,setSignIn] = useState(true)
    console.log(signIn)
    const toggleVisibility = () => setIsVisible(!isVisible)
    return (
        <div className="flex relative h-full">
            <div className="flex-shrink-0  w-[70%] fundo"></div>
            <div className=" w-full flex-shrink-1  py-12 px-12 ">
                <div className="flex items-center gap-2">
                    <img className="w-12 h-12" src="/logo.png" alt="logo" />
                    <span className=" font-bold">Global Bruno</span>
                </div>
                <form action="" className="py-12  flex flex-col gap-12">
                    <h2 className="font-bold">{signIn ? 'entre na sua conta': 'Cadastre-se'}</h2>
                    <div className=" flex flex-col  gap-5">
                    {!signIn &&  <Input
                            labelPlacement="outside"
                            type="text"
                            placeholder="Entre com email ou com telefone"
                            radius="sm"
                            label={'Nome'}
                            variant="faded"
                            size="md"
                            className="max-w-xs !rounded-md"
                        />}
                        <Input
                            labelPlacement="outside"
                            type="text"
                            placeholder="Entre com email ou com telefone"
                            radius="sm"
                            label={signIn? 'login': 'Email'}
                            variant="faded"
                            size="md"
                            className="max-w-xs !rounded-md"
                        />
                       
                        <Input
                            label="Password"
                            size="md"
                            radius="sm"
                            labelPlacement="outside"
                            variant="faded"
                            placeholder="Enter your password"
                            endContent={
                                <button
                                    className="focus:outline-none"
                                    type="button"
                                    onClick={toggleVisibility}
                                >
                                    {isVisible ? (
                                        <FaEye className="text-2xl text-default-400 pointer-events-none" />
                                    ) : (
                                        <FaEye className="text-2xl text-default-400 pointer-events-none" />
                                    )}
                                </button>
                            }
                            type={isVisible ? 'text' : 'password'}
                            className="max-w-xs !rounded-md "
                        />
                        <div className=" flex justify-between items-center">
                            <Switch
                                defaultSelected
                                className="font-bold"
                                size="sm"
                            >
                                lembre-se
                            </Switch>
                            <a className=' text-xs text-blue-700' href="">esqueceu a senha?</a>
                        </div>
                        <Button>Entre na conta</Button>
                        
                        <div className='flex justify-between items-center'>

                       <span>{signIn ? 'Não tem um conta':'Já tem uma conta?'}</span>
                        <span className=' text-xs text-blue-700' onClick={()=>setSignIn(!signIn)}>{signIn ? 'Cria uma conta': 'Faça o login'}</span>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}

from typing import Optional, List
from mongoengine.fields import EmailField
from pydantic import BaseModel

class AgentRegister(BaseModel):
    first_name : str
    last_name : str
    phone_no : str
    email_id : str
    username : str
    address : str
    city : str
    password : str
    website_url : str
    gst_no : str
    years_in_industry : Optional[int]
    directors : Optional[List[str]] = None
    service_des : str
    toogle_point : Optional[int] = None
    status : Optional[str] = None
    time_rating : Optional[float] = None
    on_ground_rating : Optional[float] = None
    overall_rating : Optional[float] = None
    subscription_type : str
    banners : Optional[List[str]] = None
    packages : Optional[List[str]] = None
    tickers : Optional[List[str]] = None

class AddAgentBanner(BaseModel):
    header : str
    package_cost : int
    price_inclusive : List[str]
    inclusions : List[str]
    exclusions : List[str]
    overview : str
    bitly_link : Optional[str] = None
    status : Optional[str] = None

class AddAgentEvent(BaseModel):
    header : str
    location : str
    description : str
    event_date : str
    event_time : str
    no_of_pax : int
    cost : int
    discount : float 
    incharge_name : str
    incharge_phone : int
    email_id : str
    status : str

class AddAgentPackageCities(BaseModel):
    city_name : str
    no_of_days : int

class AddAgentPackage(BaseModel):
    destination : str
    package_cost : int
    type_of_package : str
    price_inclusive : List[str]
    inclusions : List[str]
    exclusions : List[str]
    city_reference : List[AddAgentPackageCities]
    overview : str
    status : str

class GetQuoteGetIn(BaseModel):
    data: dict

class AddAgentTicker(BaseModel):
    ticker: str
    
class EditAgentProfile(BaseModel):
    first_name : str
    last_name : str
    username : str
    email_id : str
    profile_pic_url : str
    
class AgentChangePassword(BaseModel):
    old_password : str
    new_password : str
    
class CustomerQouteResponse(BaseModel):
    price: int 
    no_of_pax: int
    trip_date: str
    response_text: str = None
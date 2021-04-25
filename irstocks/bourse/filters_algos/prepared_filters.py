import json
import requests
from bourse.models import Shares_Specifications


def filter(filter_kind):
    
    if filter_kind != '':

        try :
            if filter_kind == "maximum_neg_pos_final":
            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (pd1)==(tmin)&&(pc)==(pl)){
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_queue":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (pl) == (tmin) && (zd1) ==0){
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "sell_queue":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (pl)== (tmax) && (zo1) !=0){
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_enter1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (tvol)>1.25*[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0)
                                {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_enter2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (tvol)>1.5*[is6]&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "co_to_real_cod1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (ct).Buy_I_Volume>0.6*(tvol)&&(ct).Sell_N_Volume>0.6*(tvol)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>((ct).Sell_I_Volume/(ct).Sell_CountI))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "co_seller_5more_than_co_buyer":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if( (ct).Sell_CountN>=5*((ct).Buy_CountN))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "prediction_tomorrow":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tno)>50&&(tvol)>(bvol)&&(bvol)<=7000000&&(plp)>=(pcp)+1.5&&(eps)>0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_volume_5more_sell":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if(((qd1)+(qd2)+(qd3))>(4 * ((qo1)+(qo2)+(qo3))) && (pl)<(pc))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "up_hammer":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if(( (pmin)==(pf)) && ((pmax)-(pmin)) *0.1 > (Math.abs((pl)-(pf))) && (pl) != (pf))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "less_basis_volume":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if(((pf)>=1.02*(py)) && ((pc)>=(py)) && (100*(((pmax)-(pmin))/(pc))>2) && (bvol)<1000000 && (pcp)>0.5)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "volume_increase":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            var tv6=function(){
                            var vol1=[ih][0].QTotTran5J;
                            var n;
                            for(n=1;n<5;n++)
                            vol1=vol1+[ih][n].QTotTran5J;
                            return vol1;
                            }
                            var tv14=function(){
                            var vol2=[ih][6].QTotTran5J;
                            var m;
                            for(m=7;m<14;m++)
                            vol2=vol2+[ih][m].QTotTran5J;
                            return vol2;
                            }
                            var minv14=function(){
                            var min=[ih][0].QTotTran5J;
                            var a;
                            for(a=1;a<14;a++)
                            {
                            if(min>[ih][a].QTotTran5J)
                                min=[ih][a].QTotTran5J;
                            }
                            return min;
                            }
                            var maxp52=function(){
                            var max1=[ih][0].PriceMax;
                            var b;
                            for(b=1;b<52;b++)
                            {
                            if(max1<[ih][b].PriceMax)
                                max1=[ih][b].PriceMax;
                            }
                            return max1;
                            };
                            if( tv6() > tv14() && (pc)<0.9*maxp52() && minv14()>0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "up_clock_pattern":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pl)>=(pc)*1.03)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })

            elif filter_kind == "month_price_floor":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            var MinPrice=function(){
                            var min=[ih][0].PriceMin;
                            var ipos;
                            for(ipos=0;ipos<30;ipos++)
                                if(min>[ih][ipos].PriceMin)
                                    min=[ih][ipos].PriceMin;
                            return min;
                            };
                            if((pl)<MinPrice())
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "price_floor_increase_capital":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((Math.min( [ih][1].PriceMin , [ih][2].PriceMin , [ih][3].PriceMin , [ih][4].PriceMin , [ih][5].PriceMin , [ih][6].PriceMin , [ih][7].PriceMin , [ih][8].PriceMin , [ih][9].PriceMin , [ih][10].PriceMin , [ih][11].PriceMin , [ih][12].PriceMin , [ih][13].PriceMin , [ih][14].PriceMin , [ih][15].PriceMin , [ih][16].PriceMin , [ih][17].PriceMin , [ih][18].PriceMin , [ih][19].PriceMin , [ih][20].PriceMin , [ih][21].PriceMin , [ih][22].PriceMin , [ih][23].PriceMin , [ih][24].PriceMin , [ih][25].PriceMin , [ih][26].PriceMin , [ih][27].PriceMin , [ih][28].PriceMin , [ih][29].PriceMin , [ih][30].PriceMin , [ih][31].PriceMin , [ih][32].PriceMin , [ih][33].PriceMin , [ih][34].PriceMin , [ih][35].PriceMin , [ih][36].PriceMin , [ih][37].PriceMin , [ih][38].PriceMin , [ih][39].PriceMin , [ih][40].PriceMin , [ih][41].PriceMin , [ih][42].PriceMin , [ih][43].PriceMin , [ih][44].PriceMin , [ih][45].PriceMin , [ih][46].PriceMin , [ih][47].PriceMin , [ih][48].PriceMin , [ih][49].PriceMin , [ih][50].PriceMin , [ih][51].PriceMin , [ih][52].PriceMin , [ih][53].PriceMin , [ih][54].PriceMin , [ih][55].PriceMin , [ih][56].PriceMin , [ih][57].PriceMin , [ih][58].PriceMin , [ih][59].PriceMin ))> ( ( Math.min( (pmin) , [ih][1].PriceMin , [ih][2].PriceMin , [ih][3].PriceMin )) ) &&(tvol) >= (bvol) &&(tvol) >200000)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "up_trend_channel_starting":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if(((pl)<((pf)-((pf)-(pmin))/2) && (pl)>((pmin)+((pf)-(pmin))/4) && (plp)<=1 && (tno)>10 && (pf)>(pmin) && (pf)>(py)) || ((pf)<(py) && (plp)<1 && (tno)>10 && (pl)>(py)) || ((pl)>1.01*(pf) && (tno)>10 && (pf)>1.01*(py) && (pl)!=(tmax)) || ((pl)>1.02*(pf) && (tno)>10 && (pl)!=(tmax)) || ((pf)<1.01*(pmin) && (plp)<=1 && (tno)>10 && (pl)>1.02*(pmin) ))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "sell_queue_last_3days":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)>(pf)&&(pmin)==(pmax)&&(pmin)==(pl)&&[ih][0].PriceYesterday>[ih][0].PriceFirst&&[ih][0].PriceMin==[ih][0].PriceMax&&[ih][0].PriceMin==[ih][0].PDrCotVal&&[ih][1].PriceYesterday>[ih][1].PriceFirst&&[ih][1].PriceMin==[ih][1].PriceMax&&[ih][1].PriceMin==[ih][1].PDrCotVal)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_queue_last_3days":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(pmin)==(pmax)&&(pmin)==(pl)&&[ih][0].PriceYesterday<[ih][0].PriceFirst&&[ih][0].PriceMin==[ih][0].PriceMax&&[ih][0].PriceMin==[ih][0].PDrCotVal&&[ih][1].PriceYesterday<[ih][1].PriceFirst&&[ih][1].PriceMin==[ih][1].PriceMax&&[ih][1].PriceMin==[ih][1].PDrCotVal)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "candle_inverted_hammer":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pc)>(pl)&&(pmax)>(pmin)&&(py)>(pl)&&(py)>=(pf)&&(pl)>(pmin)&&(pl)>(pf)&&(pl)/(pf)<1.015&&(pl)/(pf)>1.005&&(pmax)>(pl)&&(tno)>1)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "candle_doji":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pmin)<(pl)&&(pl)==(pf)&&(pl)/(pf)<1.005&&(pf)>(pc)&&(pl)>(pc))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "down_to_up_price":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pcp)<-3&&(plp)>-3)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_queue_starting1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((po1)<=(tmax)&&(po1)>=(tmax)-1&&(pd1)<(tmax))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_queue_starting2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pl)>=0.994*(tmax)&&(qo1)>0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_queue_starting3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((plp)>+4.6&&(qd1)>0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "buy_queue_starting4":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pl)>=(tmax)-6&&(pl)<=(tmax)&&(po1)<=(tmax)&&(zo1)!=0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "up_to_down_today":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pf)>(py)&&(pl)<(py))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "down_to_up_today":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((pf)<(py)&&(pl)>(py))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "suspect_volume1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)> [is5] && (tvol)>2*[is6])
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })

            elif filter_kind == "today_volume_2more_monthly_volume":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            var i
                            var sum30=0
                            var avg30
                            for(i=0;i<30;i++){
                            sum30=sum30+ [ih][i].QTotTran5J
                            }
                            avg30=Math.round(sum30/30)
                            
                            if ((tvol)>2*avg30 && (tvol)!=0 )
                            {
                                (cfield0) = Math.round((tvol)/avg30)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "down_to_up_trend":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if(((pl)<((pf)-((pf)-(pmin))/2)&&(pl)>((pmin)+((pf)-(pmin))/4)&&(plp)<=1&&(tno)>10&&(pf)>(pmin)&&(pf)>(py)) || ((pf)<(py)&&(plp)<1&&(tno)>10&&(pl)>(py)) || ((pl)>1.01*(pf)&&(tno)>10&&(pf)>1.01*(py)&&(pl)!=(tmax)) || ((pl)>1.02*(pf)&&(tno)>10&&(pl)!=(tmax)) || ((pf)<1.01*(pmin)&&(plp)<=1&&(tno)>10&&(pl)>1.02*(pmin)))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "co_to_real_cod2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((ct).Buy_I_Volume>0.7*(tvol)&&(ct).Sell_N_Volume>0.7*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "co_buyer_2more_co_seller":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((ct).Buy_CountN>=2*((ct).Sell_CountN)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>((ct).Sell_I_Volume/(ct).Sell_CountI))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "real_to_co_cod1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "real_to_co_cod2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((ct).Buy_N_Volume>0.7*(tvol)&&(ct).Sell_I_Volume>0.7*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_enter3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(py)<(pmax)&&(tvol)>1.5*(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0&&(py)<(pc)&&(py)<(pl))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_enter_co_tp_real_cod1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(py)<(pmax)&&(tvol)>1.5*(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0&&(ct).Buy_I_Volume>0.5*(tvol)&&(ct).Sell_N_Volume>0.5*(tvol)&&(py)<(pc)&&(py)<(pl))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_enter_co_tp_real_cod2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>1.5*[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0&&(ct).Buy_I_Volume>0.5*(tvol)&&(ct).Sell_N_Volume>0.5*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_enter_co_tp_real_cod3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>1.5*[is6]&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0&&(ct).Buy_I_Volume>0.5*(tvol)&&(ct).Sell_N_Volume>0.5*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_exit1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(py)<(pmax)&&(tvol)>1.5*(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0&&(py)>(pc)&&(py)>(pl))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_exit2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>1.5*[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_exit3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>1.5*[is6]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0)
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_exit_co_to_real_cod1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(py)<(pmax)&&(tvol)>1.5*(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol)&&(py)>(pc)&&(py)>(pl))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_exit_co_to_real_cod2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>1.5*[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "smart_money_exit_co_to_real_cod3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>1.5*[is6]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)<=(pc)&&(plp)<0&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "exit_money1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(py)<(pmax)&&(tvol)>([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(py)<(pc)&&(py)<(pl))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "exit_money2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "exit_money3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>[is6]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "exit_money_co_to_real_cod1":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((py)<(pf)&&(py)<(pmax)&&(tvol)>([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol)&&(py)<(pc)&&(py)<(pl))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "exit_money_co_to_real_cod2":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>[is5]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            elif filter_kind == "exit_money_co_to_real_cod3":            
                req = requests.post("http://sourcearena.ir/api/cfield_filter.php",
                    json={"token": "36f3d0f1d4ea646bc316b380375a3c33", "code": """
                            true == function(){

                            if((tvol)>[is6]&&((ct).Buy_I_Volume/(ct).Buy_CountI)<((ct).Sell_I_Volume/(ct).Sell_CountI)&&(ct).Buy_N_Volume>0.5*(tvol)&&(ct).Sell_I_Volume>0.5*(tvol))
                            {
                                (cfield0) = (pl)+ '&&';
                                return true;
                                            }

                                }()

                                """, "type": 0
                            })
            api = json.loads(req.content)
            share_list = Shares_Specifications.objects.all()
        
            result = []
            share_names = []
            for item_api in api:
                for item in share_list:
                    if item_api["symbol"] == item.NAME:
                        # temp_dict = {}
                        # # smart_money1 = api[0]["name"]
                        # temp_dict["name"] = item.NAME
                        # temp_dict["trading_volume"] = item.TRADE_VOLUME
                        # temp_dict["final_price_change"] = item.FINAL_PRICE_CHANGE_PERCENT
                        # temp_dict["close_price_change"] = item.CLOSE_PRICE_CHANGE_PERCENT
                        # temp_dict["type"] = item.TYPE
                        # temp_dict["pe"] = item.PE      
                        # result.append(temp_dict)
                        share_names.append(item.NAME)

        except Exception as e: 
            share_names = ''
            result = ''
            value = "Error"
    else:
        share_names = ''
        result = ''

   
    return {'result': result, 'share_names': share_names}
from django.urls import path, include

from api.views import ConversationRate, StatusDistribution, CategoryTypePerformance, FilteredAggregation

urlpatterns = [
    path("conversion-rate/", ConversationRate.as_view(), name="conversion_rate"),
    path("status-distribution/", StatusDistribution.as_view(), name="status_distribution"),
    path("category-type-performance/", CategoryTypePerformance.as_view(), name="category_type_performance"),
    path("filtered-aggregation/", FilteredAggregation.as_view(), name="filtered_aggregation"),

]

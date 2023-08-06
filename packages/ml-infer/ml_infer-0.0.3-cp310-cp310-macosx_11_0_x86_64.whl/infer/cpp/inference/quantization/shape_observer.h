#pragma once

#include <torch/extension.h>

#include "disjoint_set.h"
#include "params.h"

using namespace torch::jit;

namespace inference::quantization::shape_observer {

typedef c10::optional<std::vector<c10::optional<int64_t>>> shape_t;

class ShapeObserver {
   private:
    shape_t shape;

    std::shared_ptr<params::Params> params;

   public:
    /* Constructors */
    ShapeObserver(std::shared_ptr<params::Params>& params_) : shape(), params(params_) {}
    ShapeObserver(std::shared_ptr<params::Params>& params_, shape_t shape_) : shape(shape_), params(params_) {}

    /* Functions that are called on the tensor */
    void observe(torch::Tensor& t);

    /* Accessors */
    shape_t get_shape();

    /* Determmines tensor grouping */
    static void make_groups(disjoint_set::DisjointSet<const Value*>& shape_groups, const Value* tensor);

    /* Serialization */
    using State = std::tuple<shape_t>;
    State serialize();
    static ShapeObserver deserialize(std::shared_ptr<params::Params>& params_, const State& state);
};

}  // namespace inference::quantization::shape_observer
